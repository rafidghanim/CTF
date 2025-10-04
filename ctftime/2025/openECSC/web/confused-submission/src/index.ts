import { Elysia } from "elysia";
import { html } from "@elysiajs/html";
import { readFileSync } from "fs";
import { join } from "path";
import Handlebars from "handlebars";
import { starteAdminBot } from "./adminBot";

const vorlagenVerzeichnis = join(process.cwd(), "vorlagen");
const startseitenVorlage = Handlebars.compile(readFileSync(join(vorlagenVerzeichnis, "startseite.html"), "utf-8"));
const flaggeVorlage = Handlebars.compile(readFileSync(join(vorlagenVerzeichnis, "flagge.html"), "utf-8"));
const administratorVorlage = Handlebars.compile(readFileSync(join(vorlagenVerzeichnis, "administrator.html"), "utf-8"));
const verzierungenVorlage = readFileSync(join(vorlagenVerzeichnis, "verzierungen.css"), "utf-8");

const besucherZahlen = new Map<string, number>();
const standardKoepflein = {
  "Content-Security-Policy": "default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; style-src 'self' fonts.googleapis.com; font-src fonts.gstatic.com;",
  "Content-Type": "text/html; charset=utf-8",
};

const app = new Elysia()
.use(html())
.get("/", ({ query }) => {
  const benutzername = query.benutzername || "Gast";
  const istGast = benutzername === "Guest";
  const currentCount = besucherZahlen.get(benutzername) || 0;
  besucherZahlen.set(benutzername, currentCount + 1);

  const vorlagenDaten = {
    benutzername,
    istGast,
    zeigeBegruessung: !istGast,
    besucherZahlen: besucherZahlen.get(benutzername),
    aktuelleZeit: new Date().toLocaleString()
  };

  const gerudertesHTML = startseitenVorlage(vorlagenDaten);

  return new Response(gerudertesHTML, {
    headers: standardKoepflein
  });
})
// ZUTUN: Flaggen einsendung implementieren
.get("/flag", ({ query }) => {
  const benutzername = query.benutzername || "Anonymer";
  const flagge = query.flagge || "Keine Flagge übermittelt";

  const vorlagenDaten = {
    benutzername,
    flagge,
    aktuelleZeit: new Date().toLocaleString()
  };

  const gerudertesHTML = flaggeVorlage(vorlagenDaten);

  return new Response(gerudertesHTML, {
    headers: standardKoepflein
  });
})
// Flaggen absendung testen
.post("/admin", async ({ body }) => {
  const formularDaten = body as any;
  const benutzername = formularDaten?.benutzername || "Unknown";

  console.log(`🤖 Admin roboter gestartet von benutzer: ${benutzername}`);

  starteAdminBot(benutzername).catch(error => {
    console.error('❌ Admin roboter is kaputt:', error);
  });
  
  const templateData = {
    benutzername,
    aktuelleZeit: new Date().toLocaleString()
  };

  const gerudertesHTML = administratorVorlage(templateData);

  return new Response(gerudertesHTML, {
    headers: standardKoepflein
  });
})
// verzierungen laden
.get("/verzierungen.css", () => {
  return new Response(verzierungenVorlage, {
    headers: {
      "Content-Type": "text/css; charset=utf-8",
    }
  });
})
.listen(3000);

console.log(
  `🦊 Elysia läuft unter ${app.server?.hostname}:${app.server?.port}`
);
