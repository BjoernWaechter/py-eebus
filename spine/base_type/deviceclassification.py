# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.deviceclassification import DeviceClassificationStringType
from spine.union_type.deviceclassification import PowerSourceType
from types import NoneType
from spine import array_2_dict


class DeviceClassificationUserDataType: # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationUserDataType -> ComplexType
    def __init__(
            self,
            user_node_identification: DeviceClassificationStringType = None,
            user_label: LabelType = None,
            user_description: DescriptionType = None,
    ):
        super().__init__()
        
        self.user_node_identification = user_node_identification
        self.user_label = user_label
        self.user_description = user_description

        if not isinstance(self.user_node_identification, DeviceClassificationStringType | NoneType):
            raise TypeError("user_node_identification is not of type DeviceClassificationStringType")
        
        if not isinstance(self.user_label, LabelType | NoneType):
            raise TypeError("user_label is not of type LabelType")
        
        if not isinstance(self.user_description, DescriptionType | NoneType):
            raise TypeError("user_description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.user_node_identification is not None:
            msg_data.append({"userNodeIdentification": self.user_node_identification.get_data()})
        if self.user_label is not None:
            msg_data.append({"userLabel": self.user_label.get_data()})
        if self.user_description is not None:
            msg_data.append({"userDescription": self.user_description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.user_node_identification is not None:
            result_str += f"{sep}userNodeIdentification: {self.user_node_identification}"
            sep = ", "
        if self.user_label is not None:
            result_str += f"{sep}userLabel: {self.user_label}"
            sep = ", "
        if self.user_description is not None:
            result_str += f"{sep}userDescription: {self.user_description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                user_node_identification=data_dict.get('userNodeIdentification'),
                user_label=data_dict.get('userLabel'),
                user_description=data_dict.get('userDescription'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceClassificationManufacturerDataType: # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationManufacturerDataType -> ComplexType
    def __init__(
            self,
            device_name: DeviceClassificationStringType = None,
            device_code: DeviceClassificationStringType = None,
            serial_number: DeviceClassificationStringType = None,
            software_revision: DeviceClassificationStringType = None,
            hardware_revision: DeviceClassificationStringType = None,
            vendor_name: DeviceClassificationStringType = None,
            vendor_code: DeviceClassificationStringType = None,
            brand_name: DeviceClassificationStringType = None,
            power_source: PowerSourceType = None,
            manufacturer_node_identification: DeviceClassificationStringType = None,
            manufacturer_label: LabelType = None,
            manufacturer_description: DescriptionType = None,
    ):
        super().__init__()
        
        self.device_name = device_name
        self.device_code = device_code
        self.serial_number = serial_number
        self.software_revision = software_revision
        self.hardware_revision = hardware_revision
        self.vendor_name = vendor_name
        self.vendor_code = vendor_code
        self.brand_name = brand_name
        self.power_source = power_source
        self.manufacturer_node_identification = manufacturer_node_identification
        self.manufacturer_label = manufacturer_label
        self.manufacturer_description = manufacturer_description

        if not isinstance(self.device_name, DeviceClassificationStringType | NoneType):
            raise TypeError("device_name is not of type DeviceClassificationStringType")
        
        if not isinstance(self.device_code, DeviceClassificationStringType | NoneType):
            raise TypeError("device_code is not of type DeviceClassificationStringType")
        
        if not isinstance(self.serial_number, DeviceClassificationStringType | NoneType):
            raise TypeError("serial_number is not of type DeviceClassificationStringType")
        
        if not isinstance(self.software_revision, DeviceClassificationStringType | NoneType):
            raise TypeError("software_revision is not of type DeviceClassificationStringType")
        
        if not isinstance(self.hardware_revision, DeviceClassificationStringType | NoneType):
            raise TypeError("hardware_revision is not of type DeviceClassificationStringType")
        
        if not isinstance(self.vendor_name, DeviceClassificationStringType | NoneType):
            raise TypeError("vendor_name is not of type DeviceClassificationStringType")
        
        if not isinstance(self.vendor_code, DeviceClassificationStringType | NoneType):
            raise TypeError("vendor_code is not of type DeviceClassificationStringType")
        
        if not isinstance(self.brand_name, DeviceClassificationStringType | NoneType):
            raise TypeError("brand_name is not of type DeviceClassificationStringType")
        
        if not isinstance(self.power_source, PowerSourceType | NoneType):
            raise TypeError("power_source is not of type PowerSourceType")
        
        if not isinstance(self.manufacturer_node_identification, DeviceClassificationStringType | NoneType):
            raise TypeError("manufacturer_node_identification is not of type DeviceClassificationStringType")
        
        if not isinstance(self.manufacturer_label, LabelType | NoneType):
            raise TypeError("manufacturer_label is not of type LabelType")
        
        if not isinstance(self.manufacturer_description, DescriptionType | NoneType):
            raise TypeError("manufacturer_description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.device_name is not None:
            msg_data.append({"deviceName": self.device_name.get_data()})
        if self.device_code is not None:
            msg_data.append({"deviceCode": self.device_code.get_data()})
        if self.serial_number is not None:
            msg_data.append({"serialNumber": self.serial_number.get_data()})
        if self.software_revision is not None:
            msg_data.append({"softwareRevision": self.software_revision.get_data()})
        if self.hardware_revision is not None:
            msg_data.append({"hardwareRevision": self.hardware_revision.get_data()})
        if self.vendor_name is not None:
            msg_data.append({"vendorName": self.vendor_name.get_data()})
        if self.vendor_code is not None:
            msg_data.append({"vendorCode": self.vendor_code.get_data()})
        if self.brand_name is not None:
            msg_data.append({"brandName": self.brand_name.get_data()})
        if self.power_source is not None:
            msg_data.append({"powerSource": self.power_source.get_data()})
        if self.manufacturer_node_identification is not None:
            msg_data.append({"manufacturerNodeIdentification": self.manufacturer_node_identification.get_data()})
        if self.manufacturer_label is not None:
            msg_data.append({"manufacturerLabel": self.manufacturer_label.get_data()})
        if self.manufacturer_description is not None:
            msg_data.append({"manufacturerDescription": self.manufacturer_description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_name is not None:
            result_str += f"{sep}deviceName: {self.device_name}"
            sep = ", "
        if self.device_code is not None:
            result_str += f"{sep}deviceCode: {self.device_code}"
            sep = ", "
        if self.serial_number is not None:
            result_str += f"{sep}serialNumber: {self.serial_number}"
            sep = ", "
        if self.software_revision is not None:
            result_str += f"{sep}softwareRevision: {self.software_revision}"
            sep = ", "
        if self.hardware_revision is not None:
            result_str += f"{sep}hardwareRevision: {self.hardware_revision}"
            sep = ", "
        if self.vendor_name is not None:
            result_str += f"{sep}vendorName: {self.vendor_name}"
            sep = ", "
        if self.vendor_code is not None:
            result_str += f"{sep}vendorCode: {self.vendor_code}"
            sep = ", "
        if self.brand_name is not None:
            result_str += f"{sep}brandName: {self.brand_name}"
            sep = ", "
        if self.power_source is not None:
            result_str += f"{sep}powerSource: {self.power_source}"
            sep = ", "
        if self.manufacturer_node_identification is not None:
            result_str += f"{sep}manufacturerNodeIdentification: {self.manufacturer_node_identification}"
            sep = ", "
        if self.manufacturer_label is not None:
            result_str += f"{sep}manufacturerLabel: {self.manufacturer_label}"
            sep = ", "
        if self.manufacturer_description is not None:
            result_str += f"{sep}manufacturerDescription: {self.manufacturer_description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device_name=data_dict.get('deviceName'),
                device_code=data_dict.get('deviceCode'),
                serial_number=data_dict.get('serialNumber'),
                software_revision=data_dict.get('softwareRevision'),
                hardware_revision=data_dict.get('hardwareRevision'),
                vendor_name=data_dict.get('vendorName'),
                vendor_code=data_dict.get('vendorCode'),
                brand_name=data_dict.get('brandName'),
                power_source=data_dict.get('powerSource'),
                manufacturer_node_identification=data_dict.get('manufacturerNodeIdentification'),
                manufacturer_label=data_dict.get('manufacturerLabel'),
                manufacturer_description=data_dict.get('manufacturerDescription'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceClassificationUserDataElementsType: # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationUserDataElementsType -> ComplexType
    def __init__(
            self,
            user_node_identification: ElementTagType = None,
            user_label: ElementTagType = None,
            user_description: ElementTagType = None,
    ):
        super().__init__()
        
        self.user_node_identification = user_node_identification
        self.user_label = user_label
        self.user_description = user_description

        if not isinstance(self.user_node_identification, ElementTagType | NoneType):
            raise TypeError("user_node_identification is not of type ElementTagType")
        
        if not isinstance(self.user_label, ElementTagType | NoneType):
            raise TypeError("user_label is not of type ElementTagType")
        
        if not isinstance(self.user_description, ElementTagType | NoneType):
            raise TypeError("user_description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.user_node_identification is not None:
            msg_data.append({"userNodeIdentification": self.user_node_identification.get_data()})
        if self.user_label is not None:
            msg_data.append({"userLabel": self.user_label.get_data()})
        if self.user_description is not None:
            msg_data.append({"userDescription": self.user_description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.user_node_identification is not None:
            result_str += f"{sep}userNodeIdentification: {self.user_node_identification}"
            sep = ", "
        if self.user_label is not None:
            result_str += f"{sep}userLabel: {self.user_label}"
            sep = ", "
        if self.user_description is not None:
            result_str += f"{sep}userDescription: {self.user_description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                user_node_identification=data_dict.get('userNodeIdentification'),
                user_label=data_dict.get('userLabel'),
                user_description=data_dict.get('userDescription'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceClassificationManufacturerDataElementsType: # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationManufacturerDataElementsType -> ComplexType
    def __init__(
            self,
            device_name: ElementTagType = None,
            device_code: ElementTagType = None,
            serial_number: ElementTagType = None,
            software_revision: ElementTagType = None,
            hardware_revision: ElementTagType = None,
            vendor_name: ElementTagType = None,
            vendor_code: ElementTagType = None,
            brand_name: ElementTagType = None,
            power_source: ElementTagType = None,
            manufacturer_node_identification: ElementTagType = None,
            manufacturer_label: ElementTagType = None,
            manufacturer_description: ElementTagType = None,
    ):
        super().__init__()
        
        self.device_name = device_name
        self.device_code = device_code
        self.serial_number = serial_number
        self.software_revision = software_revision
        self.hardware_revision = hardware_revision
        self.vendor_name = vendor_name
        self.vendor_code = vendor_code
        self.brand_name = brand_name
        self.power_source = power_source
        self.manufacturer_node_identification = manufacturer_node_identification
        self.manufacturer_label = manufacturer_label
        self.manufacturer_description = manufacturer_description

        if not isinstance(self.device_name, ElementTagType | NoneType):
            raise TypeError("device_name is not of type ElementTagType")
        
        if not isinstance(self.device_code, ElementTagType | NoneType):
            raise TypeError("device_code is not of type ElementTagType")
        
        if not isinstance(self.serial_number, ElementTagType | NoneType):
            raise TypeError("serial_number is not of type ElementTagType")
        
        if not isinstance(self.software_revision, ElementTagType | NoneType):
            raise TypeError("software_revision is not of type ElementTagType")
        
        if not isinstance(self.hardware_revision, ElementTagType | NoneType):
            raise TypeError("hardware_revision is not of type ElementTagType")
        
        if not isinstance(self.vendor_name, ElementTagType | NoneType):
            raise TypeError("vendor_name is not of type ElementTagType")
        
        if not isinstance(self.vendor_code, ElementTagType | NoneType):
            raise TypeError("vendor_code is not of type ElementTagType")
        
        if not isinstance(self.brand_name, ElementTagType | NoneType):
            raise TypeError("brand_name is not of type ElementTagType")
        
        if not isinstance(self.power_source, ElementTagType | NoneType):
            raise TypeError("power_source is not of type ElementTagType")
        
        if not isinstance(self.manufacturer_node_identification, ElementTagType | NoneType):
            raise TypeError("manufacturer_node_identification is not of type ElementTagType")
        
        if not isinstance(self.manufacturer_label, ElementTagType | NoneType):
            raise TypeError("manufacturer_label is not of type ElementTagType")
        
        if not isinstance(self.manufacturer_description, ElementTagType | NoneType):
            raise TypeError("manufacturer_description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.device_name is not None:
            msg_data.append({"deviceName": self.device_name.get_data()})
        if self.device_code is not None:
            msg_data.append({"deviceCode": self.device_code.get_data()})
        if self.serial_number is not None:
            msg_data.append({"serialNumber": self.serial_number.get_data()})
        if self.software_revision is not None:
            msg_data.append({"softwareRevision": self.software_revision.get_data()})
        if self.hardware_revision is not None:
            msg_data.append({"hardwareRevision": self.hardware_revision.get_data()})
        if self.vendor_name is not None:
            msg_data.append({"vendorName": self.vendor_name.get_data()})
        if self.vendor_code is not None:
            msg_data.append({"vendorCode": self.vendor_code.get_data()})
        if self.brand_name is not None:
            msg_data.append({"brandName": self.brand_name.get_data()})
        if self.power_source is not None:
            msg_data.append({"powerSource": self.power_source.get_data()})
        if self.manufacturer_node_identification is not None:
            msg_data.append({"manufacturerNodeIdentification": self.manufacturer_node_identification.get_data()})
        if self.manufacturer_label is not None:
            msg_data.append({"manufacturerLabel": self.manufacturer_label.get_data()})
        if self.manufacturer_description is not None:
            msg_data.append({"manufacturerDescription": self.manufacturer_description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_name is not None:
            result_str += f"{sep}deviceName: {self.device_name}"
            sep = ", "
        if self.device_code is not None:
            result_str += f"{sep}deviceCode: {self.device_code}"
            sep = ", "
        if self.serial_number is not None:
            result_str += f"{sep}serialNumber: {self.serial_number}"
            sep = ", "
        if self.software_revision is not None:
            result_str += f"{sep}softwareRevision: {self.software_revision}"
            sep = ", "
        if self.hardware_revision is not None:
            result_str += f"{sep}hardwareRevision: {self.hardware_revision}"
            sep = ", "
        if self.vendor_name is not None:
            result_str += f"{sep}vendorName: {self.vendor_name}"
            sep = ", "
        if self.vendor_code is not None:
            result_str += f"{sep}vendorCode: {self.vendor_code}"
            sep = ", "
        if self.brand_name is not None:
            result_str += f"{sep}brandName: {self.brand_name}"
            sep = ", "
        if self.power_source is not None:
            result_str += f"{sep}powerSource: {self.power_source}"
            sep = ", "
        if self.manufacturer_node_identification is not None:
            result_str += f"{sep}manufacturerNodeIdentification: {self.manufacturer_node_identification}"
            sep = ", "
        if self.manufacturer_label is not None:
            result_str += f"{sep}manufacturerLabel: {self.manufacturer_label}"
            sep = ", "
        if self.manufacturer_description is not None:
            result_str += f"{sep}manufacturerDescription: {self.manufacturer_description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device_name=data_dict.get('deviceName'),
                device_code=data_dict.get('deviceCode'),
                serial_number=data_dict.get('serialNumber'),
                software_revision=data_dict.get('softwareRevision'),
                hardware_revision=data_dict.get('hardwareRevision'),
                vendor_name=data_dict.get('vendorName'),
                vendor_code=data_dict.get('vendorCode'),
                brand_name=data_dict.get('brandName'),
                power_source=data_dict.get('powerSource'),
                manufacturer_node_identification=data_dict.get('manufacturerNodeIdentification'),
                manufacturer_label=data_dict.get('manufacturerLabel'),
                manufacturer_description=data_dict.get('manufacturerDescription'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



