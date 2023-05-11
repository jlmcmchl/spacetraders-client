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


class ShipFrame(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.
    """


    class MetaOapg:
        required = {
            "symbol",
            "moduleSlots",
            "requirements",
            "fuelCapacity",
            "name",
            "description",
            "mountingPoints",
        }
        
        class properties:
            
            
            class symbol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "FRAME_PROBE": "PROBE",
                        "FRAME_DRONE": "DRONE",
                        "FRAME_INTERCEPTOR": "INTERCEPTOR",
                        "FRAME_RACER": "RACER",
                        "FRAME_FIGHTER": "FIGHTER",
                        "FRAME_FRIGATE": "FRIGATE",
                        "FRAME_SHUTTLE": "SHUTTLE",
                        "FRAME_EXPLORER": "EXPLORER",
                        "FRAME_MINER": "MINER",
                        "FRAME_LIGHT_FREIGHTER": "LIGHT_FREIGHTER",
                        "FRAME_HEAVY_FREIGHTER": "HEAVY_FREIGHTER",
                        "FRAME_TRANSPORT": "TRANSPORT",
                        "FRAME_DESTROYER": "DESTROYER",
                        "FRAME_CRUISER": "CRUISER",
                        "FRAME_CARRIER": "CARRIER",
                    }
                
                @schemas.classproperty
                def PROBE(cls):
                    return cls("FRAME_PROBE")
                
                @schemas.classproperty
                def DRONE(cls):
                    return cls("FRAME_DRONE")
                
                @schemas.classproperty
                def INTERCEPTOR(cls):
                    return cls("FRAME_INTERCEPTOR")
                
                @schemas.classproperty
                def RACER(cls):
                    return cls("FRAME_RACER")
                
                @schemas.classproperty
                def FIGHTER(cls):
                    return cls("FRAME_FIGHTER")
                
                @schemas.classproperty
                def FRIGATE(cls):
                    return cls("FRAME_FRIGATE")
                
                @schemas.classproperty
                def SHUTTLE(cls):
                    return cls("FRAME_SHUTTLE")
                
                @schemas.classproperty
                def EXPLORER(cls):
                    return cls("FRAME_EXPLORER")
                
                @schemas.classproperty
                def MINER(cls):
                    return cls("FRAME_MINER")
                
                @schemas.classproperty
                def LIGHT_FREIGHTER(cls):
                    return cls("FRAME_LIGHT_FREIGHTER")
                
                @schemas.classproperty
                def HEAVY_FREIGHTER(cls):
                    return cls("FRAME_HEAVY_FREIGHTER")
                
                @schemas.classproperty
                def TRANSPORT(cls):
                    return cls("FRAME_TRANSPORT")
                
                @schemas.classproperty
                def DESTROYER(cls):
                    return cls("FRAME_DESTROYER")
                
                @schemas.classproperty
                def CRUISER(cls):
                    return cls("FRAME_CRUISER")
                
                @schemas.classproperty
                def CARRIER(cls):
                    return cls("FRAME_CARRIER")
            name = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class moduleSlots(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class mountingPoints(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class fuelCapacity(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
        
            @staticmethod
            def requirements() -> typing.Type['ShipRequirements']:
                return ShipRequirements
        
            @staticmethod
            def condition() -> typing.Type['ShipCondition']:
                return ShipCondition
            __annotations__ = {
                "symbol": symbol,
                "name": name,
                "description": description,
                "moduleSlots": moduleSlots,
                "mountingPoints": mountingPoints,
                "fuelCapacity": fuelCapacity,
                "requirements": requirements,
                "condition": condition,
            }
    
    symbol: MetaOapg.properties.symbol
    moduleSlots: MetaOapg.properties.moduleSlots
    requirements: 'ShipRequirements'
    fuelCapacity: MetaOapg.properties.fuelCapacity
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    mountingPoints: MetaOapg.properties.mountingPoints
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moduleSlots"]) -> MetaOapg.properties.moduleSlots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mountingPoints"]) -> MetaOapg.properties.mountingPoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fuelCapacity"]) -> MetaOapg.properties.fuelCapacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> 'ShipRequirements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["condition"]) -> 'ShipCondition': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "description", "moduleSlots", "mountingPoints", "fuelCapacity", "requirements", "condition", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moduleSlots"]) -> MetaOapg.properties.moduleSlots: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mountingPoints"]) -> MetaOapg.properties.mountingPoints: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fuelCapacity"]) -> MetaOapg.properties.fuelCapacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> 'ShipRequirements': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["condition"]) -> typing.Union['ShipCondition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "description", "moduleSlots", "mountingPoints", "fuelCapacity", "requirements", "condition", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        moduleSlots: typing.Union[MetaOapg.properties.moduleSlots, decimal.Decimal, int, ],
        requirements: 'ShipRequirements',
        fuelCapacity: typing.Union[MetaOapg.properties.fuelCapacity, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        mountingPoints: typing.Union[MetaOapg.properties.mountingPoints, decimal.Decimal, int, ],
        condition: typing.Union['ShipCondition', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShipFrame':
        return super().__new__(
            cls,
            *_args,
            symbol=symbol,
            moduleSlots=moduleSlots,
            requirements=requirements,
            fuelCapacity=fuelCapacity,
            name=name,
            description=description,
            mountingPoints=mountingPoints,
            condition=condition,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.ship_condition import ShipCondition
from openapi_client.model.ship_requirements import ShipRequirements
