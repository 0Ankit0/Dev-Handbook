# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: GraphQL Quick Reference

### Schema Definition Language (SDL)

```graphql
# Scalar types: String, Int, Float, Boolean, ID
# ! means non-nullable (required)

# Object type — a resource with fields
type User {
  id: ID!
  name: String!
  email: String!
  age: Int
  posts: [Post!]!     # List of non-null Posts (list can be empty)
  role: UserRole!
}

# Enum type
enum UserRole {
  ADMIN
  EDITOR
  VIEWER
}

# Input type — used for mutation arguments (cannot use object types as input)
input CreateUserInput {
  name: String!
  email: String!
  role: UserRole = VIEWER   # default value
}

# Interface — fields all implementing types must have
interface Node {
  id: ID!
}

type Post implements Node {
  id: ID!
  title: String!
  body: String!
  author: User!
  publishedAt: String
}

# Union — one of several types (no common fields)
union SearchResult = User | Post | Comment

# Root types
type Query {
  user(id: ID!): User          # nullable — returns null if not found
  users: [User!]!              # non-nullable list
  search(query: String!): [SearchResult!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: CreateUserInput!): User
  deleteUser(id: ID!): Boolean!
}

type Subscription {
  userCreated: User!
  postPublished(authorId: ID): Post!
}
```

### Query Syntax

```graphql
# Basic query with field selection
query GetUser {
  user(id: "123") {
    id
    name
    email
    posts {
      id
      title
    }
  }
}

# Query with variables (recommended over inline values)
query GetUser($userId: ID!) {
  user(id: $userId) {
    name
    email
  }
}

# Variables sent separately as JSON:
# { "userId": "123" }

# Aliases — fetch same field with different arguments
query GetTwoUsers {
  alice: user(id: "1") { name email }
  bob: user(id: "2") { name email }
}

# Fragments — reusable field sets
fragment UserBasic on User {
  id
  name
  email
}

query GetUsers {
  user(id: "1") { ...UserBasic }
}

# Inline fragments — for unions and interfaces
query SearchContent($q: String!) {
  search(query: $q) {
    ... on User { name email }
    ... on Post { title body }
  }
}

# Directives
query GetUser($withPosts: Boolean!) {
  user(id: "1") {
    name
    posts @include(if: $withPosts) { title }
    role @skip(if: false)
  }
}
```

### Mutation Syntax

```graphql
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
    email
    role
  }
}

# Variables:
# {
#   "input": {
#     "name": "Alice",
#     "email": "alice@example.com",
#     "role": "EDITOR"
#   }
# }
```

### Subscription Syntax

```graphql
subscription OnUserCreated {
  userCreated {
    id
    name
    email
  }
}
```

### Python Resolver Example (Strawberry)

```python
import strawberry
from typing import List, Optional

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        # Fetch from database
        return db.get_user(id)

    @strawberry.field
    def users(self) -> List[User]:
        return db.get_all_users()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        return db.create_user(name=name, email=email)

schema = strawberry.Schema(query=Query, mutation=Mutation)
```

### JavaScript Resolver Example (Apollo Server)

```js
const { ApolloServer, gql } = require('@apollo/server');

const typeDefs = gql`
  type Query {
    user(id: ID!): User
  }
  type User {
    id: ID!
    name: String!
  }
`;

const resolvers = {
  Query: {
    user: async (parent, { id }, context) => {
      return context.dataSources.userAPI.getUser(id);
    },
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
```

---

## Appendix B: Common Anti-Patterns and Fixes

### N+1 Problem

```text
PROBLEM: For each of 100 posts, you fetch the author separately.
  → 1 query for posts + 100 queries for authors = 101 queries

SOLUTION: Use DataLoader (batching + caching)
  → 1 query for posts + 1 batched query for all authors = 2 queries
```

```js
const DataLoader = require('dataloader');

// Batch function — receives array of IDs, returns array of users
const userLoader = new DataLoader(async (userIds) => {
  const users = await db.getUsersByIds(userIds);
  // Must return in same order as input IDs
  return userIds.map(id => users.find(u => u.id === id));
});

// In resolver — DataLoader batches concurrent calls
const resolvers = {
  Post: {
    author: (post, _, { loaders }) => loaders.user.load(post.authorId),
  },
};
```

### Query Depth Limiting

```js
const depthLimit = require('graphql-depth-limit');

const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [depthLimit(5)],  // max 5 levels of nesting
});
```

### Query Complexity Analysis

```js
const { createComplexityLimitRule } = require('graphql-validation-complexity');

const server = new ApolloServer({
  validationRules: [
    createComplexityLimitRule(1000),  // reject if complexity > 1000
  ],
});
```

---

## Appendix C: Glossary

**Schema**
The contract between client and server. Defines all types, queries, mutations, and subscriptions available. Written in SDL (Schema Definition Language).

**Resolver**
A function that fetches the data for a specific field. Every field in a GraphQL schema has a resolver. If you don't provide one, the default resolver returns the property with the same name from the parent object.

**Query**
A GraphQL operation that reads data. Like a GET request in REST. Queries can request exactly the fields they need — no more, no less.

**Mutation**
A GraphQL operation that modifies data (create, update, delete). Like POST/PUT/DELETE in REST. Mutations can also return data.

**Subscription**
A long-lived GraphQL operation that pushes real-time updates to the client via WebSocket. The server sends data whenever a relevant event occurs.

**Fragment**
A reusable piece of a query — a set of fields that can be included in multiple queries. Reduces repetition.

**Introspection**
GraphQL's built-in mechanism for querying the schema itself. Tools like GraphiQL and Apollo Studio use introspection to show you what types and operations are available.

**DataLoader**
A utility for batching and caching database calls in resolvers. Solves the N+1 problem by collecting multiple load() calls and executing them as a single batch query.

**Federation**
An approach to composing multiple GraphQL schemas from different services into a single unified API. Apollo Federation is the dominant implementation.

**Persisted Queries**
A technique where clients send only a hash identifier instead of the full query string. Improves performance and security (the server only accepts pre-approved queries).

---

## Appendix D: Resources

- [GraphQL Spec](https://spec.graphql.org/) — the official specification
- [How to GraphQL](https://www.howtographql.com/) — free full-stack tutorial
- [Apollo Docs](https://www.apollographql.com/docs/) — most popular GraphQL implementation
- [Strawberry (Python)](https://strawberry.rocks/) — modern Python GraphQL library
- [graphql-js](https://github.com/graphql/graphql-js) — reference implementation
