# Sentence Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/sentence-count?text=`

## Example

Request:
`/v1/sentence-count?text=Hello%20world.%20How%20are%20you%3F%20Great!`

Response:
```json
{
  "input": "Hello world. How are you? Great!",
  "sentence_count": 3
}
