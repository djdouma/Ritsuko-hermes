const PUBLIC_KEY_PEM = `-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEjkS4v5q7l/j9QWV6ErIY1iPMFqnA
hl6H8hNxyX9TX3m9WnEEFfxDOk0ZF3TPm6lb5MGB/gQ5iK3iUOImN7t/AQ==
-----END PUBLIC KEY-----
`;

export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (url.pathname === "/.well-known/appspecific/com.tesla.3p.public-key.pem") {
      return new Response(PUBLIC_KEY_PEM + "\n", {
        headers: {
          "Content-Type": "application/x-pem-file",
          "Cache-Control": "public, max-age=86400"
        }
      });
    }

    return new Response("Not found\n", { status: 404 });
  }
};
