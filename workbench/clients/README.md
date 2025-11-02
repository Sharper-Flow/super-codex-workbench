Clients live here. Each client should:
- Use `httpx` for HTTP calls
- Provide small, focused functions with strict Pydantic models (inherit `StrictBaseModel` when applicable)
- Read config (base URL, API key) from environment variables
- Avoid side effects; return structured results

Naming convention:
- File: `workbench/clients/<service>.py`
- Env vars: `<SERVICE>_BASE_URL`, `<SERVICE>_API_KEY`

