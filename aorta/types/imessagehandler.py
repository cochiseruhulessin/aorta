# Copyright (C) 2016-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from .command import Command
from .event import Event
from .itransaction import ITransaction
from .messagemetadata import MessageMetadata


class IMessageHandler:
    __module__: str = 'aorta.types'

    def __init__(
        self,
        publisher: ITransaction,
        metadata: MessageMetadata
    ):
        ...

    def issue(self, command: Command) -> None: ...
    def publish(self, event: Event) -> None: ...
    async def handle(self, *args: Any) -> Any: ...