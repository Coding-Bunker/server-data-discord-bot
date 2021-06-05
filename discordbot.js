const Discord = require('discord.js');
const client = new Discord.Client();

const { SiteClient, buildModularBlock } = require('datocms-client');
const clientCMS = new SiteClient(process.env.CMS_KEY);

client.on('ready', () => {

  let members = client.guilds.cache.get(process.env.GUILD_ID).members;

  let users = 0;
  members.cache.each(m => {
    if(!m.user.bot)
      users++;
  });

  clientCMS.items
  .update(process.env.ITEM_ID, {
      sections:
      [
          buildModularBlock({
              itemType: process.env.ITEM_TYPE,
              numeroMembri: users,
            })
      ]
  })
  .then((item) => {
      console.log(item);
  })
  .catch((error) => {
      console.error(error);
  });
});

client.login(process.env.DISCORD_BOT_KEY);