from ship.enums import *
from ship.message import *


class TestTimer:

    def test_init_connectionhello(self):
        msgs = [
            ConnectionHello(phase=ConnectionHelloPhaseType.READY),
            ConnectionHello(phase=ConnectionHelloPhaseType.PENDING, prolongationrequest=True),
            ConnectionHello(phase=ConnectionHelloPhaseType.ABORTED),
            ConnectionHello(phase=ConnectionHelloPhaseType.READY, waiting=1000),
        ]

        assert msgs[0].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"ready"},{"waiting":60000}]}'
        assert msgs[
                   1].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"pending"},{"waiting":60000},{"prolongationRequest":true}]}'
        assert msgs[2].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"aborted"},{"waiting":60000}]}'
        assert msgs[3].get_msg_bytes() == b'\x01{"connectionHello":[{"phase":"ready"},{"waiting":1000}]}'

    def test_init_messageprotocolhandshake(self):
        msgs = [
            MessageProtocolHandshake(handshaketype=ProtocolHandshakeTypeType.ANNOUNCEMAX),
            MessageProtocolHandshake(handshaketype=ProtocolHandshakeTypeType.SELECT, formats=MessageProtocolFormatsType(
                format=[MessageProtocolFormatType("JSON-UTF16")])),
            MessageProtocolHandshake(handshaketype=ProtocolHandshakeTypeType.ANNOUNCEMAX,
                                     version=[{"major": 2}, {"minor": 1}])
        ]

        assert msgs[
                   0].get_msg_bytes() == b'\x01{"messageProtocolHandshake":[{"handshakeType":"announceMax"},{"version":[{"major":1},' \
                                         b'{"minor":0}]},{"formats":[{"format":["JSON-UTF8"]}]}]}'
        assert msgs[
                   1].get_msg_bytes() == b'\x01{"messageProtocolHandshake":[{"handshakeType":"select"},{"version":[{"major":1},' \
                                         b'{"minor":0}]},{"formats":[{"format":["JSON-UTF16"]}]}]}'
        assert msgs[
                   2].get_msg_bytes() == (b'\x01{"messageProtocolHandshake":[{"handshakeType":"announceMax"},'
                                          b'{"version":[{"major":2},{"minor":1}]},{"formats":[{"format":["JSON-UTF8"]}]}]}')

    def test_init_accessmethods(self):
        msgs = [
            AccessMethods(id="TESTBRAND11314235241414"),
            AccessMethods(id="TESTBRAND11314235241414", dns="dns1"),
            AccessMethods(id="TESTBRAND11314235241414", dns="dns1", dnssd_mdns="m1"),
        ]

        assert msgs[0].get_msg_bytes() == b'\x01{"accessMethods":[{"id":"TESTBRAND11314235241414"}]}'
        assert msgs[1].get_msg_bytes() == b'\x01{"accessMethods":[{"id":"TESTBRAND11314235241414"},{"dns":"dns1"}]}'
        assert msgs[
                   2].get_msg_bytes() == (b'\x01{"accessMethods":[{"id":"TESTBRAND11314235241414"},'
                                          b'{"dnsSd_mDns":"m1"},{"dns":"dns1"}]}')

    def test_init_connectionpinstate(self):
        msgs = [
            ConnectionPinState(PinStateType.NONE),
            ConnectionPinState(PinStateType.REQUIRED),
            ConnectionPinState(PinStateType.PINOK),
            ConnectionPinState(PinStateType.OPTIONAL),
        ]

        assert msgs[0].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"none"}]}'
        assert msgs[1].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"required"}]}'
        assert msgs[2].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"pinOk"}]}'
        assert msgs[3].get_msg_bytes() == b'\x01{"connectionPinState":[{"pinState":"optional"}]}'

    def test_init_accessmethodsrequest(self):
        msg = AccessMethodsRequest()

        assert msg.get_msg_bytes() == b'\x01{"accessMethodsRequest":[]}'

    def test_init_data(self):
        msgs = [
            Data(header=HeaderType(protocolid=ProtocolIdType()), payload="MY_DATA")
        ]

        assert msgs[0].get_msg_bytes() == b'\x02{"data":[{"header":[{"protocolId":"ee1.0"}]},{"payload":"MY_DATA"}]}'

    def test_init_connectionclose(self):
        msgs = [
            ConnectionClose(phase=ConnectionClosePhaseType.CONFIRM),
            ConnectionClose(phase=ConnectionClosePhaseType.ANNOUNCE),
            ConnectionClose(phase=ConnectionClosePhaseType.ANNOUNCE, maxtime=30),
        ]

        assert msgs[0].get_msg_bytes() == b'\x03{"connectionClose":[{"phase":"confirm"}]}'
        assert msgs[1].get_msg_bytes() == b'\x03{"connectionClose":[{"phase":"announce"}]}'
        assert msgs[2].get_msg_bytes() == b'\x03{"connectionClose":[{"phase":"announce"},{"maxTime":30}]}'
