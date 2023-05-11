# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.     # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ShipRole(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The registered role of the ship
    """


    class MetaOapg:
        enum_value_to_name = {
            "FABRICATOR": "FABRICATOR",
            "HARVESTER": "HARVESTER",
            "HAULER": "HAULER",
            "INTERCEPTOR": "INTERCEPTOR",
            "EXCAVATOR": "EXCAVATOR",
            "TRANSPORT": "TRANSPORT",
            "REPAIR": "REPAIR",
            "SURVEYOR": "SURVEYOR",
            "COMMAND": "COMMAND",
            "CARRIER": "CARRIER",
            "PATROL": "PATROL",
            "SATELLITE": "SATELLITE",
            "EXPLORER": "EXPLORER",
            "REFINERY": "REFINERY",
        }
    
    @schemas.classproperty
    def FABRICATOR(cls):
        return cls("FABRICATOR")
    
    @schemas.classproperty
    def HARVESTER(cls):
        return cls("HARVESTER")
    
    @schemas.classproperty
    def HAULER(cls):
        return cls("HAULER")
    
    @schemas.classproperty
    def INTERCEPTOR(cls):
        return cls("INTERCEPTOR")
    
    @schemas.classproperty
    def EXCAVATOR(cls):
        return cls("EXCAVATOR")
    
    @schemas.classproperty
    def TRANSPORT(cls):
        return cls("TRANSPORT")
    
    @schemas.classproperty
    def REPAIR(cls):
        return cls("REPAIR")
    
    @schemas.classproperty
    def SURVEYOR(cls):
        return cls("SURVEYOR")
    
    @schemas.classproperty
    def COMMAND(cls):
        return cls("COMMAND")
    
    @schemas.classproperty
    def CARRIER(cls):
        return cls("CARRIER")
    
    @schemas.classproperty
    def PATROL(cls):
        return cls("PATROL")
    
    @schemas.classproperty
    def SATELLITE(cls):
        return cls("SATELLITE")
    
    @schemas.classproperty
    def EXPLORER(cls):
        return cls("EXPLORER")
    
    @schemas.classproperty
    def REFINERY(cls):
        return cls("REFINERY")
