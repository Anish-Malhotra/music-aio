from fastapi import FastAPI
from graphene import Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from app.server.gql.mutations import Mutation
from app.server.gql.queries import Query


# GQL Schema
schema = Schema(query=Query, mutation=Mutation)

# Webserver init
app = FastAPI()
graphene_app = GraphQLApp(
    on_get=make_graphiql_handler(),
    schema=schema,
)
