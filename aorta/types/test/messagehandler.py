# Copyright (C) 2016-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest

import aorta


__all__: list[str] = [
    'test_handle_success',
    'test_issue_command',
    'test_publish_event',
]


@pytest.mark.asyncio
async def test_handle_success(
    transaction: aorta.types.ITransaction,
    message: aorta.types.Publishable,
    MessageHandler: type[aorta.types.IMessageHandler]
):
    envelope = message.envelope()
    handler = MessageHandler(
        metadata=envelope.metadata,
        publisher=transaction
    )
    assert await handler.handle(envelope.message) == 'foo'


@pytest.mark.asyncio
async def test_issue_command(
    publisher: aorta.types.IPublisher,
    transport: aorta.NullTransport,
    message: aorta.types.Publishable,
    command: aorta.Command,
    MessageHandler: type[aorta.types.IMessageHandler]
):
    envelope = message.envelope()
    async with aorta.Transaction(publisher) as tx:
        assert envelope.metadata.correlation_id is not None
        handler = MessageHandler(
            metadata=envelope.metadata,
            publisher=tx
        )
        handler.issue(command)

    assert len(transport.sent) == 1
    assert transport.sent[0].metadata.correlation_id != tx.correlation_id
    assert transport.sent[0].metadata.correlation_id == envelope.metadata.correlation_id


@pytest.mark.asyncio
async def test_publish_event(
    publisher: aorta.types.IPublisher,
    transport: aorta.NullTransport,
    message: aorta.types.Publishable,
    event: aorta.Event,
    MessageHandler: type[aorta.types.IMessageHandler]
):
    envelope = message.envelope()
    async with aorta.Transaction(publisher) as tx:
        handler = MessageHandler(
            metadata=envelope.metadata,
            publisher=tx
        )
        handler.publish(event)

    assert len(transport.sent) == 1
    assert transport.sent[0].metadata.correlation_id != tx.correlation_id
    assert transport.sent[0].metadata.correlation_id == envelope.metadata.correlation_id