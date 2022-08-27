import Fastify from "fastify";

const port = 8000;

const f = Fastify({
  logger: true,
});

f.get("/", (req, res) => {
  res.send("Hello there");
});

f.listen({ port }, (err, address) => {
  if (err) {
    f.log.error(err);
    process.exit(1);
  }
  console.log(`Server is now listening on ${address}`);
});
