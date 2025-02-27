import pytest

from ship.base_type import HeaderType as ShipHeader
from ship.message import Data, ProtocolIdType
from spine.enums.commandframe import CmdClassifierType
from spine.simple_type.commandframe import MsgCounterType
from spine.simple_type.commondatatypes import SpecificationVersionType, AddressDeviceType, AddressEntityType, \
    AddressFeatureType
from spine.base_message import SpineMessage
from spine.base_type.commandframe import CmdType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.base_type.datagram import DatagramType, PayloadType, HeaderType


class TestSpine:

    def test_empty_data(self):

        h = ShipHeader(protocol_id=ProtocolIdType())
        msg = Data(header=h, payload=DatagramType(header=HeaderType(), payload=PayloadType()))

        assert msg.get_msg_bytes() == (b'\x02{"data":[{"header":[{"protocolId":"ee1.0"}]},{"payload":[{"header":[]},{"payload":[]}]}]}')
        assert str(msg) == 'Data(2, header: protocolId: ee1.0, payload: header: , payload: )'

    def test_first_message(self):
        h = ShipHeader(protocol_id=ProtocolIdType())
        msg = DatagramType(
                    header=HeaderType(
                        specification_version=SpecificationVersionType("1.3.0"),
                        address_source=FeatureAddressType(
                            device=AddressDeviceType("d:_i:21381_Heatbox2-B92F89"),
                            entity=[AddressEntityType(0)],
                            feature=AddressFeatureType(0)
                        ),
                        address_destination=FeatureAddressType(
                            entity=[AddressEntityType(0)],
                            feature=AddressFeatureType(0)
                        ),
                        msg_counter=MsgCounterType(76),
                        cmd_classifier=CmdClassifierType.read,
                        ack_request=True
                    ),
                    payload=PayloadType(
                        cmd=[]
                    )
                )

        assert msg.get_data() == [{
                        "header":[{"specificationVersion":"1.3.0"},{"addressSource":[{"device":"d:_i:21381_Heatbox2-B92F89"},{"entity":[0]},{"feature":0}]},{"addressDestination":[{"entity":[0]},{"feature":0}]},{"msgCounter":76},{"cmdClassifier":"read"},{"ackRequest":True}]
                    },{
                        "payload":[{"cmd":[[{"nodeManagementDetailedDiscoveryData":[]}]]}]}
        ]