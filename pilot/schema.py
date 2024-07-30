import graphene

import pilotapp.schema



class Query(pilotapp.schema.Query,graphene.ObjectType):
    pass

class Mutation(pilotapp.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)

