# pylint: skip-file
import fastapi
import pydantic
import uvicorn

import aorta
from aorta.transport.http import MessageReceiver


app = MessageReceiver(allowed_hosts=['*'])
publisher = aorta.EventPublisher(None)

class OnMutation(aorta.EventListener):

    class Meta:
        handles = [
            ('picqer.com/v1', 'Mutation')
        ]


aorta.register(OnMutation)

message = publisher.prepare({
    'apiVersion': "picqer.com/v1",
    'kind': "Mutation",
    'data': {'bar': "Foo"}
})

print(message.json())

if __name__ == '__main__':
    uvicorn.run('__main__:app',
        host="127.0.0.1",
        port=5000,
        log_level="debug",
        reload=True
    )
