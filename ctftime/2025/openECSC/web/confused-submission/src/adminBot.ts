import { chromium } from 'playwright';

export async function starteAdminBot(ausgeloestVon: string): Promise<void> {
  const FLAGGE = process.env.FLAG || "flagge{standard_admin_flagge}";
  
  console.log(`🤖 Admin Bot gestartet von: ${ausgeloestVon}`);
  
  const stöberer = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  try {
    const seite = await stöberer.newPage();
    
    // Besuche Startseite und setze Benutzername
    await seite.goto('http://localhost:3000');
    await seite.fill('input[name="benutzername"]', ausgeloestVon);
    await seite.click('button[type="submit"]');
    await seite.waitForTimeout(1000);
    
    // Sende die Flagge ab
    await seite.fill('input[name="flagge"]', FLAGGE);
    await seite.click('.flag-btn');
    
    console.log(`🎯 Admin hat Flagge abgesendet: ${FLAGGE}`);

  } finally {
    await stöberer.close();
  }
}
