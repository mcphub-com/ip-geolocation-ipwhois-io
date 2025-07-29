import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/xakageminato/api/ip-geolocation-ipwhois-io'

mcp = FastMCP('ip-geolocation-ipwhois-io')

@mcp.tool()
def jsonendpoint(ip: Annotated[Union[str, None], Field(description='{ip} can be an IPv4 or IPv6 address, or none to use the current IP address.')] = None) -> dict: 
    '''Detailed information on our website: https://ipwhois.io/documentation'''
    url = 'https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/'
    headers = {'x-rapidapi-host': 'ip-geolocation-ipwhois-io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ip': ip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
