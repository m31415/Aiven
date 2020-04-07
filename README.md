# Aiven
Cloud Selection

# Install node_modules
`cd client && npm install`

# Build React-Client
`cd client  && npm run build`

# Build App
`docker build -t aiven .`

# Run App
`docker run -p 80:80 aiven`

# Run Server Tests
`docker run aiven pytest`

# Run Client Tests
`cd client && npm run test`
