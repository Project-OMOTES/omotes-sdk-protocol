# OMOTES SDK Protocol
This package contains the protobuf (proto3) message definitions in Python for the OMOTES SDK protocol.
This protocol specifies job communication between OMOTES and any user of the SDK.

# Example
```python
import uuid
import datetime
from omotes_sdk_protocol.job_pb2 import JobSubmission

some_message = JobSubmission(uuid=uuid.uuid4(),
                             timeout_ms=round(datetime.timedelta(seconds=10).total_seconds() * 1000),
                             workflow_type="grow_optimizer",
                             esdl=b'your raw esdl encoded as UTF-8 here')
```
