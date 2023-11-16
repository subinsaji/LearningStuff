from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from collections import defaultdict 

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://api.github.com/graphql", headers={'Authorization': 'bearer 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'})  # noqa: E501

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query

query = gql(
    """
query {
  repository(owner: "subinsaji", name: "TestGitHubActions") {
    pullRequest(number: 24) {
      closingIssuesReferences(first: 1) {
        edges {
          node {
            id
          }
        }
      }
      author { ... on User {id} }
    }
  }
}
"""
)

# execute query
result_query = client.execute(query)
print(result_query)

repository = result_query["repository"]
pullRequest = repository["pullRequest"]
author = pullRequest["author"]
author_id = author["id"]
closingIssuesReferences = pullRequest["closingIssuesReferences"]
edges = closingIssuesReferences["edges"]
node = edges[0]
node = node["node"]
assignable_id = node["id"]

print(author_id, type(author_id))
print(assignable_id, type(assignable_id))

# author_id = str(author_id)
# assignable_id = str(assignable_id)

mutation_addComment = gql(
    """
mutation ($assignable_id: ID!){
      addComment(input:{subjectId: $assignable_id , body:"Hello! This comment is a mutation using graph ql"}) {
        clientMutationId
      }
    }
    """  # noqa: E501
)

mutation_addAssigneesToAssignable = gql(
    """
mutation ($assignable_id: ID!, $author_id: [ID!]! ){
      addAssigneesToAssignable(input:{assignableId: $assignable_id, assigneeIds: $author_id }) {
        clientMutationId
      }
    }
    """     # noqa: E501
)

params = {
  "assignable_id" : assignable_id,
  "author_id" : author_id
}

# Execute the query on the transport
result_addComment = client.execute(mutation_addComment, variable_values=params)
result_addAssigneesToAssignable = client.execute(mutation_addAssigneesToAssignable, variable_values=params)  # noqa: E501


print(result_addComment)
print(result_addAssigneesToAssignable)


