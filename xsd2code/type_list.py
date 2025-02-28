import os

import xsd2code
import networkx as nx

import xsd2code


class TypeList:

    def __init__(self):
        self.types: list[xsd2code.DataType] = []
        self._type_dict = {}

    def get_or_create(self, add_type: xsd2code.DataType):

        if add_type.fq_name in self._type_dict:
            return self._type_dict[add_type.fq_name]

        self.types.append(add_type)
        self._type_dict[add_type.fq_name] = add_type

        return add_type

    def get_by_name(self, type_name, throw_exe=True):

        if type_name in self._type_dict:
            return self._type_dict[type_name]
        # namespace, type_name = type_name.split(":")
        #
        # for existing_type in self.types:
        #     if existing_type.namespace == namespace and existing_type.type_name == type_name:
        #         return existing_type
        if throw_exe:
            raise RuntimeError(f"Type not found: {type_name}")
        else:
            return None

    def sort_by_name(self):
        self.types.sort(key=lambda x: x.fq_name)

    def get_all_by_type(self, data_type, key_by=None, filters: str = None):
        if key_by:
            result = {}
        else:
            result = []

        if filters:
            filter_attribute, filter_value = filters.split("=")
        else:
            filter_attribute, filter_value = None, None

        for existing_type in self.types:
            if isinstance(existing_type, data_type):
                if filters is None or getattr(existing_type, filter_attribute) == filter_value:
                    if key_by:
                        if getattr(existing_type, key_by) not in result:
                            result[getattr(existing_type, key_by)] = {"types": [], "imports": ["{{ test }}"]}

                        result[getattr(existing_type, key_by)]["types"].append(existing_type)
                    else:
                        result["types"].append(existing_type)

        return result

    def set_template_options_by_type(self, data_type, module, file_name, jinja_template, filters: str = None):
        if filters:
            filter_attribute, filter_value = filters.split("=")
        else:
            filter_attribute, filter_value = None, None

        for existing_type in self.types:
            if isinstance(existing_type, data_type):
                if filters is None or getattr(existing_type, filter_attribute) == filter_value:
                    existing_type.set_module(module)
                    existing_type.set_file_name(file_name)
                    existing_type.set_jinja_template(jinja_template)

    def get_types_without_template_options(self):
        result = []
        for existing_type in self.types:
            if not existing_type.module or not existing_type.get_full_path():
                result.append(existing_type)

        return result

    @staticmethod
    def sort_types_by_dependencies(type_list):
        nx_graph = nx.DiGraph()
        keyed_input = {}
        input_size = len(type_list)

        for ele in type_list:

            nx_graph.add_node(ele.fq_name)
            keyed_input[ele.fq_name] = ele

            #print(ele.depend_on_types)
            for dep in ele.depend_on_types:
                nx_graph.add_edge(ele.fq_name, dep.fq_name)
                #nx_graph.add_edge(dep, ele.fq_name)

        sorted_graph = list(reversed(list(nx.topological_sort(nx_graph))))
        sorted_types = []
        for type_name in sorted_graph:
            if type_name in keyed_input:
                sorted_types.append(keyed_input[type_name])

        if input_size != len(sorted_types):
            raise RuntimeError(f"Sorting failed {input_size} != {len(sorted_types)}")

        return sorted_types

    def write_all_files(self):

        write_destinations = {}

        dest_folder = []

        for existing_type in self.types:
            dest_path = existing_type.get_full_path()

            jinja_template = existing_type.get_jinja_template()
            if dest_path and jinja_template:
                dest_folder.append(os.sep.join(dest_path.split(os.sep)[0:-1]))

                if dest_path not in write_destinations:
                    folder = dest_path.split("/")[0]
                    write_destinations[dest_path] = {
                        "folder": folder,
                        "jinja_template": existing_type.get_jinja_template(),
                        "types": [],
                        "depend_on_types": []
                    }

                if write_destinations[dest_path]["jinja_template"] != existing_type.get_jinja_template():
                    raise RuntimeError(f"Same destination file but different jinja templates: dest_path: {dest_path} templates {write_destinations[dest_path]['jinja_template']} != {existing_type.get_jinja_template()}")

                write_destinations[dest_path]["types"].append(existing_type)
                #print(f"{existing_type} - {[d.class_name for d in existing_type.depend_on_types]}")
                write_destinations[dest_path]["depend_on_types"] += existing_type.depend_on_types

        for fol in list(set(dest_folder)):
            for (dirpath, dirnames, filenames) in os.walk(fol):
                for file in filenames:
                    if "__init__.py" not in file and ".pyc" not in file:
                        #print(f'delete: {dirpath}{os.sep}{file}')
                        os.remove(f'{dirpath}{os.sep}{file}')

        for write_dest in write_destinations:

            #print(f"{write_dest} - {[d.class_name for d in write_destinations[write_dest]['depend_on_types'] ]}")

            with open(write_dest, "w") as text_file:
                depend_on_types = list(set(write_destinations[write_dest]["depend_on_types"]))

                imports = list(set(
                    [imp.get_import() for imp in depend_on_types if imp.get_import() and imp.get_full_path() != write_dest]
                ))

                imports.sort()
                #print(write_dest)
                sorted_types = self.sort_types_by_dependencies(
                    type_list=write_destinations[write_dest]["types"]
                )

                text_file.write(write_destinations[write_dest]["jinja_template"].render(
                    folder=write_destinations[write_dest]["folder"],
                    types=sorted_types,
                    is_ship_msg_type=False,
                    imports=imports
                ))


ALL_TYPES = TypeList()
