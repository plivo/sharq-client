SharQ Client
============

SharQ client helps to define workers & exposes functions to interact with SharQ server.

## Usage

### Enqueue
```python
>>> from sharq_client import SharQClient
>>> sqc = SharQClient(host='sharq.server.plivo.com', port=80)
>>> response = sqc.enqueue(
        job_id='cea84623-be35-4368-90fa-7736570dabc4',
        payload={'message': 'hello, world'},
        interval=1000,  # in milliseconds
        queue_id='johndoe',
        queue_type='sms'  # optional.
    )
>>> print response
(201, {'status': 'queued'})
```
