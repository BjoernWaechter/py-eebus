from ship.enums import *
from ship.message import *

TEST_MESSAGES = {
    "ConnectionHello": [
        ConnectionHello(phase=ConnectionHelloPhaseType.READY),
        ConnectionHello(phase=ConnectionHelloPhaseType.PENDING, prolongation_request=True),
        ConnectionHello(phase=ConnectionHelloPhaseType.ABORTED),
        ConnectionHello(phase=ConnectionHelloPhaseType.READY, waiting=1000),
    ],
    "MessageProtocolHandshake": [
        MessageProtocolHandshake(
            handshake_type=ProtocolHandshakeTypeType.ANNOUNCEMAX,
            formats=MessageProtocolFormatsType(format=[MessageProtocolFormatType("JSON-UTF8")])),
        MessageProtocolHandshake(
            handshake_type=ProtocolHandshakeTypeType.SELECT,
            formats=MessageProtocolFormatsType(format=[MessageProtocolFormatType("JSON-UTF16")])),
        MessageProtocolHandshake(handshake_type=ProtocolHandshakeTypeType.ANNOUNCEMAX,
                                 version=Version(major=2, minor=1)),
        MessageProtocolHandshake(handshake_type=ProtocolHandshakeTypeType.ANNOUNCEMAX),
        MessageProtocolHandshake(handshake_type=ProtocolHandshakeTypeType.SELECT),
    ],
    "AccessMethods": [
        AccessMethods(id="TESTBRAND11314235241414"),
        AccessMethods(id="TESTBRAND11314235241414", dns=Dns(uri="dns1")),
        AccessMethods(id="TESTBRAND11314235241414", dns=Dns(uri="dns1"), dns_sd_m_dns=DnsSd_MDns()),
    ],
    "ConnectionPinState": [
        ConnectionPinState(PinStateType.NONE),
        ConnectionPinState(PinStateType.REQUIRED),
        ConnectionPinState(PinStateType.PINOK),
        ConnectionPinState(PinStateType.OPTIONAL),
    ],
    "AccessMethodsRequest": [
        AccessMethodsRequest()
    ],
    "Data": [
        Data(header=HeaderType(protocol_id=ProtocolIdType()), payload="MY_DATA")
    ],
    "ConnectionClose": [
        ConnectionClose(phase=ConnectionClosePhaseType.CONFIRM),
        ConnectionClose(phase=ConnectionClosePhaseType.ANNOUNCE),
        ConnectionClose(phase=ConnectionClosePhaseType.ANNOUNCE, max_time=30),
    ]

}


class TestTimer:

    def test_init_cmi(self):
        msgs = [Cmi(), Cmi(b'\x01')]

        assert msgs[0].get_msg_bytes() == b'\x00\x00'
        assert msgs[1].get_msg_bytes() == b'\x00\x01'

        assert msgs[1].msg() == b'\x01'

    def test_init_connectionhello(self):
        msgs = TEST_MESSAGES["ConnectionHello"]

        assert msgs[0].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"ready"},{"waiting":60000}]}'
        assert str(msgs[0]) == 'ConnectionHello(1, phase: ready, waiting: 60000)'

        assert msgs[1].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"pending"},{"waiting":60000},{"prolongationRequest":true}]}'
        assert str(msgs[1]) == 'ConnectionHello(1, phase: pending, waiting: 60000, prolongationRequest: True)'

        assert msgs[2].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"aborted"},{"waiting":60000}]}'
        assert str(msgs[2]) == 'ConnectionHello(1, phase: aborted, waiting: 60000)'

        assert msgs[3].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"ready"},{"waiting":1000}]}'
        assert str(msgs[3]) == 'ConnectionHello(1, phase: ready, waiting: 1000)'

    def test_init_messageprotocolhandshake(self):
        msgs = TEST_MESSAGES["MessageProtocolHandshake"]

        assert msgs[0].get_msg_bytes() == b'\x01{"messageProtocolHandshake":[{"handshakeType":"announceMax"},{"version":[{"major":1},' \
                                         b'{"minor":0}]},{"formats":[{"format":["JSON-UTF8"]}]}]}'
        assert str(msgs[0]) == "MessageProtocolHandshake(1, handshakeType: announceMax, version: major: 1, minor: 0, formats: format: JSON-UTF8)"

        assert msgs[1].get_msg_bytes() == b'\x01{"messageProtocolHandshake":[{"handshakeType":"select"},{"version":[{"major":1},' \
                                         b'{"minor":0}]},{"formats":[{"format":["JSON-UTF16"]}]}]}'
        assert str(msgs[1]) == "MessageProtocolHandshake(1, handshakeType: select, version: major: 1, minor: 0, formats: format: JSON-UTF16)"

        assert msgs[2].get_msg_bytes() == (b'\x01{"messageProtocolHandshake":[{"handshakeType":"announceMax"},'
                                          b'{"version":[{"major":2},{"minor":1}]},{"formats":[{"format":["JSON-UTF8"]}]}]}')
        assert str(msgs[2]) == "MessageProtocolHandshake(1, handshakeType: announceMax, version: major: 2, minor: 1, formats: format: JSON-UTF8)"

        assert msgs[3].get_msg_bytes() == b'\x01{"messageProtocolHandshake":[{"handshakeType":"announceMax"},{"version":[{"major":1},' \
                                         b'{"minor":0}]},{"formats":[{"format":["JSON-UTF8"]}]}]}'
        assert str(msgs[3]) == "MessageProtocolHandshake(1, handshakeType: announceMax, version: major: 1, minor: 0, formats: format: JSON-UTF8)"

        assert msgs[4].get_msg_bytes() == b'\x01{"messageProtocolHandshake":[{"handshakeType":"select"},{"version":[{"major":1},' \
                                         b'{"minor":0}]},{"formats":[{"format":["JSON-UTF8"]}]}]}'

        assert str(msgs[4]) == "MessageProtocolHandshake(1, handshakeType: select, version: major: 1, minor: 0, formats: format: JSON-UTF8)"

    def test_init_accessmethods(self):
        msgs = TEST_MESSAGES["AccessMethods"]

        assert msgs[0].get_msg_bytes() == b'\x01{"accessMethods":[{"id":"TESTBRAND11314235241414"}]}'
        assert msgs[1].get_msg_bytes() == b'\x01{"accessMethods":[{"id":"TESTBRAND11314235241414"},{"dns":[{"uri":"dns1"}]}]}'
        assert msgs[2].get_msg_bytes() == b'\x01{"accessMethods":[{"id":"TESTBRAND11314235241414"},{"dnsSd_mDns":[]},{"dns":[{"uri":"dns1"}]}]}'

    def test_init_connectionpinstate(self):
        msgs = TEST_MESSAGES["ConnectionPinState"]

        assert msgs[0].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"none"}]}'
        assert msgs[1].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"required"}]}'
        assert msgs[2].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"pinOk"}]}'
        assert msgs[3].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"optional"}]}'

    def test_init_accessmethodsrequest(self):
        msgs = TEST_MESSAGES["AccessMethodsRequest"]

        assert msgs[0].get_msg_bytes() == b'\x01{"accessMethodsRequest":[]}'

    def test_init_data(self):
        msgs = TEST_MESSAGES["Data"]

        assert msgs[0].get_msg_bytes() == b'\x02{"data":[{"header":[{"protocolId":"ee1.0"}]},{"payload":"MY_DATA"}]}'

    def test_init_connectionclose(self):
        msgs = TEST_MESSAGES["ConnectionClose"]

        assert msgs[0].get_msg_bytes() == b'\x03{"connectionClose":[{"phase":"confirm"}]}'
        assert msgs[1].get_msg_bytes() == b'\x03{"connectionClose":[{"phase":"announce"}]}'
        assert msgs[2].get_msg_bytes() == b'\x03{"connectionClose":[{"phase":"announce"},{"maxTime":30}]}'

    def test_parse_cmi(self):
        msgs = [Cmi(), Cmi(b'\x01')]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_connectionhello(self):
        msgs = TEST_MESSAGES["ConnectionHello"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_messageprotocolhandshake(self):
        msgs = TEST_MESSAGES["MessageProtocolHandshake"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_accessmethods(self):
        msgs = TEST_MESSAGES["AccessMethods"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_connectionpinstate(self):
        msgs = TEST_MESSAGES["ConnectionPinState"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_accessmethodsrequest(self):
        msgs = TEST_MESSAGES["AccessMethodsRequest"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_data(self):
        msgs = TEST_MESSAGES["Data"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    def test_parse_connectionclose(self):
        msgs = TEST_MESSAGES["ConnectionClose"]

        for msg in msgs:
            assert msg == ShipMessage.from_data(msg.get_msg_bytes())

    # def test_message_parser(self):
    #
    #     for msgtype in TEST_MESSAGES:
    #         for org_msg in TEST_MESSAGES[msgtype]:
    #             recovered_msg = ShipMessage.from_data(org_msg.get_msg_bytes())
    #
    #             assert org_msg == recovered_msg
