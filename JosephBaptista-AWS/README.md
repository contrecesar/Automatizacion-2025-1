# Serverless Application with AWS Lambda

## Usage

### Setup

To try this example, you need to run the following command first and follow the instructions:

```
serverless
```

### Deployment

To deploy the application, run the following command:

```
serverless deploy
```

Make sure you have your AWS credentials configured before running this command.

### Invocation

After a successful deployment, you can invoke the deployed function via HTTP:

```
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/hello
```

Which should result in response similar to:

```json
{ "message": "Hello! This is a simple example." }
```
