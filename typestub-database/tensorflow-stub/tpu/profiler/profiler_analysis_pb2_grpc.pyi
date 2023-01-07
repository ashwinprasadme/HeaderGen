from typing import Any

class ProfileAnalysisStub:
    NewSession: Any
    EnumSessions: Any
    GetSessionToolData: Any
    def __init__(self, channel) -> None: ...

class ProfileAnalysisServicer:
    def NewSession(self, request, context) -> None: ...
    def EnumSessions(self, request, context) -> None: ...
    def GetSessionToolData(self, request, context) -> None: ...

def add_ProfileAnalysisServicer_to_server(servicer, server) -> None: ...