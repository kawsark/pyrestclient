# Pyrestclient: A Python REST API Client

This project provides sample code to interact with Cloud hosting providers via
a REST API. This process typically involves obtaining an API authentication
token and sending HTTPS requests. Pyrestclient does not have a dependency on
provider python SDKs. It uses the Requests HTTP Library to communicate with published REST API and endpoint.

## How to use:
**Rackspace cloud**:
- Download the API client python file: `apiclient-rax.py`.
- Create a corresponding credentials file (see `sample-pyrax.creds`) and update the `credentials_file` variable in `apiclient-rax.py` with correct path.
- Edit the `REGION` variable in `apiclient-rax.py`. Default is IAD.
- Execute from command line using python: `python apiclient-rax.py`.
- Import into existing projects: `import apiclient-rax`.

Additional notes:
- Do not embed credentials in your source code. Use a separate protected credentials file instead.
- Currently retry logic is not present to allow for simplicity. 

## Built With

* [Python](https://docs.python.org/)
* [Requests](http://docs.python-requests.org/)
* [Rackspace Cloud REST API](https://developer.rackspace.com/docs/cloud-servers/quickstart/)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
