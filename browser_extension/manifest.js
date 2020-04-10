{
  "manifest_version": 2,
  "name": "Czarno na białym",
  "version": "1.0",

  "descriptions": "Wtyczka ostrzegająca użytkownika przed fake newsami (połączona ze stroną czarnonabiałym.org)",

  "icons": {
    "48": "assets/ikona.jfif"
    // "96": "icons/border-96.png"
  },

  "applications": {
    "gecko": {
      "id": "czarnonabialym@gmail.com"
    }
  },

  "content_scripts": [{
    "matches": ["*://*/*"],
    "js": ["content.js"]
  }]
}