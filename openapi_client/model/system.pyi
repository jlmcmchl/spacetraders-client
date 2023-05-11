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


class System(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "sectorSymbol",
            "x",
            "y",
            "type",
            "waypoints",
            "factions",
        }
        
        class properties:
            
            
            class symbol(
                schemas.StrSchema
            ):
                pass
            
            
            class sectorSymbol(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def type() -> typing.Type['SystemType']:
                return SystemType
            x = schemas.IntSchema
            y = schemas.IntSchema
            
            
            class waypoints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SystemWaypoint']:
                        return SystemWaypoint
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SystemWaypoint'], typing.List['SystemWaypoint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'waypoints':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SystemWaypoint':
                    return super().__getitem__(i)
            
            
            class factions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SystemFaction']:
                        return SystemFaction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SystemFaction'], typing.List['SystemFaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'factions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SystemFaction':
                    return super().__getitem__(i)
            __annotations__ = {
                "symbol": symbol,
                "sectorSymbol": sectorSymbol,
                "type": type,
                "x": x,
                "y": y,
                "waypoints": waypoints,
                "factions": factions,
            }
    
    symbol: MetaOapg.properties.symbol
    sectorSymbol: MetaOapg.properties.sectorSymbol
    x: MetaOapg.properties.x
    y: MetaOapg.properties.y
    type: 'SystemType'
    waypoints: MetaOapg.properties.waypoints
    factions: MetaOapg.properties.factions
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sectorSymbol"]) -> MetaOapg.properties.sectorSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'SystemType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waypoints"]) -> MetaOapg.properties.waypoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factions"]) -> MetaOapg.properties.factions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "sectorSymbol", "type", "x", "y", "waypoints", "factions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sectorSymbol"]) -> MetaOapg.properties.sectorSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'SystemType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waypoints"]) -> MetaOapg.properties.waypoints: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factions"]) -> MetaOapg.properties.factions: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "sectorSymbol", "type", "x", "y", "waypoints", "factions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        sectorSymbol: typing.Union[MetaOapg.properties.sectorSymbol, str, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, ],
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, ],
        type: 'SystemType',
        waypoints: typing.Union[MetaOapg.properties.waypoints, list, tuple, ],
        factions: typing.Union[MetaOapg.properties.factions, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'System':
        return super().__new__(
            cls,
            *_args,
            symbol=symbol,
            sectorSymbol=sectorSymbol,
            x=x,
            y=y,
            type=type,
            waypoints=waypoints,
            factions=factions,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.system_faction import SystemFaction
from openapi_client.model.system_type import SystemType
from openapi_client.model.system_waypoint import SystemWaypoint