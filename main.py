import discord
import json
import requests
from discord import app_commands
import typing
import sys
import asyncio
from discord.gateway import DiscordWebSocket, _log
from discord.ext.commands import bot
from datetime import timedelta
from discord.ui import Button
from discord import ButtonStyle
from discord.ui import View, Button
from datetime import datetime, timedelta
from discord import Permissions, utils
from discord import ui
import os
import time
from threading import Thread




run = "python site.py"
language = "python3"



intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

ipath = "userdata.json"
ipath2 = "サーバーID: "

BOT_TOKEN = os.environ['BOT_TOKEN']
authurl = "https://discord.com/oauth2/authorize?client_id=1204424642199031870&redirect_uri=https://restorecord.com/api/callback&response_type=code&scope=identify+guilds.join&state=1204252157180649494"

CUSTOM_COLOR = discord.Colour(int("90EE90", 16))

cooldowns = {}





@client.event
async def on_message(message):
   if message.content.startswith("!st "):
       if client.user!=message.author:
           stmsg=message.content[4:]
           await client.change_presence(activity = discord.Activity(name=str(stmsg), type=discord.ActivityType.playing))



@client.event
async def on_ready():
    print(f'This is /call! {client.user}')

@tree.command(name="call", description="認証したひと”全員”を追加する")
async def call(interaction: discord.Interaction,データサーバーid:str=None):
    try:
        if interaction.user.guild_permissions.administrator:
            zenj=open(ipath)
            zendata = json.load(zenj)

            if データサーバーid==None:
                useridj=open(f"{ipath2}{interaction.guild_id}.json")
            elif データサーバーid=="all":
                useridj=zenj
            else:
                useridj=open(f"{ipath2}{データサーバーid}.json")
            userid = json.load(useridj)
            a=b=c=d=e=f=0
            for key, value in list(userid.items()):
                addmember=eagm.add_member(access_token=zendata[key],user_id=key,guild_id=str(interaction.guild.id))
                if addmember==201:
                    a=a+1
                elif addmember==204:
                    b=b+1
                elif addmember==403:
                    c=c+1
                    del (zendata[f"{key}"])
                    del (userid[f"{key}"])
                elif addmember==429:
                    e=e+1
                elif addmember==400:
                    f=f+1
                else:
                    d=d+1

                asyncio.sleep(1)# <- TooManyRequest対策です！！おこのみの数値または必要ないなら消してください！
            if データサーバーid==None:
                json.dump(userid, open(f"{ipath2}{interaction.guild_id}.json","w"))
                json.dump(zendata, open(ipath,"w"))
            elif データサーバーid=="all":
                json.dump(userid, open(ipath,"w"))
            else:
                json.dump(userid, open(f"{ipath2}{データサーバーid}.json","w"))
                json.dump(zendata, open(ipath,"w"))

            await interaction.channel.send(f"リクエストが終わりました\n{a}人を追加\n{b}人は既に追加されていて\n{c}人の情報が失効済み\n{e}回TooManyRequest\n{f}人はこれ以上サーバーに参加できません\n{d}人は不明なエラーです")
        else:
            await interaction.response.send_message("管理者しか使えません", ephemeral=True)
            return    
    except:
        await interaction.response.send_message("DMでは使えません", ephemeral=True)


@tree.command(name="button", description="認証ボタンの表示")
async def panel_au(interaction: discord.Interaction,ロール:discord.Role,タイトル:str=None,説明:str=None):
    None
@tree.command(name="check", description="UserIDを使ってTokenを検索する")
async def check(interaction: discord.Interaction,ユーザーid:str):
    None
@tree.command(name="request1", description="UserIDとトークンを使って1人リクエストする")
async def req1(interaction: discord.Interaction,ユーザーid:str):
    None
@tree.command(name="delkey", description="該当ユーザーの情報を削除する")
async def delk(interaction: discord.Interaction,ユーザーid:str):
    None
@tree.command(name="datacheck", description="登録人数の確認")
async def datac(interaction: discord.Interaction):
    None









@client.event
async def on_disconnect():
  print("Discordから切断されました。再接続しています...")


@client.event
async def on_error(event, *args, **kwargs):
  print(f"{event}でエラーが発生しました：{sys.exc_info()}")


@client.event
async def on_ready():
  print(f'Logged in as {client.user.name} ({client.user.id})')
  await tree.sync()


@tree.command(name="commands", description="コマンドの一覧です。")
async def commands(interaction):
  embed = discord.Embed(title="コマンド一覧", color=CUSTOM_COLOR)
  embed.add_field(name="avatar", value="アバター画像を表示します。", inline=True)
  embed.add_field(name="getuserid", value="あなたのユーザーIDを表示する。", inline=True)
  embed.add_field(name="help", value="ヘルプを表示します。", inline=True)
  embed.add_field(name="ping", value="ボットのレイテンシを確認します。", inline=True)
  embed.add_field(name="say", value="指定したチャンネルにメッセージを送信する。", inline=True)
  embed.add_field(name="serverinfo", value="サーバーの詳細情報を表示します。", inline=True)
  embed.add_field(name="top", value="チャンネルの最初のメッセージを取得します", inline=True)
  embed.add_field(name="userinfo", value="ユーザーの詳細情報を表示します。", inline=True)
  embed.add_field(name="auth_panel", value="OAuth2の認証パネルを表示します。", inline=True)
  embed.add_field(name="backup", value="バックアップを開始します。", inline=True)
  embed.add_field(name="restore", value="特定のユーザーを復元します。", inline=True)
  embed.add_field(name="data_check", value="認証済み人数を確認します。", inline=True)

  await interaction.response.send_message(embed=embed, ephemeral=False)


@tree.command(name="avatar", description="アバター画像を表示します。")
@app_commands.describe(user="ユーザーを選択")
async def avatar(interaction: discord.Interaction, user: discord.User):
  if user.display_avatar:
    avatar_url = user.display_avatar.url
  else:
    avatar_url = user.default_avatar.url

  embed = discord.Embed(title=f"{user.display_name}のアバター画像",
                        color=CUSTOM_COLOR)
  embed.set_image(url=avatar_url)

  download_button = Button(style=ButtonStyle.link,
                           label="ダウンロード",
                           url=avatar_url)

  view = View()
  view.add_item(download_button)

  await interaction.response.send_message(embed=embed, view=view)


@tree.command(name='get_userid', description="ユーザーIDを取得します。")
async def getuser_id(interaction):
  await interaction.response.send_message(
      f'Your user ID is `{interaction.user.id}`.', ephemeral=False)


@tree.command(name="help", description="ヘルプを表示します。")
async def bot_help(interaction: discord.Interaction):
  message = "Created by Yukito // awakun_\n\nこのボットはもしかしたらダウンタイムがあるかも知れません。\nちなみにこのボットは他のサーバーへ導入できません。"
  await interaction.response.send_message(message, ephemeral=False)


@tree.command(name="ping", description="ボットのレイテンシを確認します。")
async def ping(interaction: discord.Interaction):
  raw_ping = client.latency
  ping = round(raw_ping * 1000)
  await interaction.response.send_message(f"Ping: {ping}ms", ephemeral=True)


@tree.command(name="say", description="指定したチャンネルにメッセージを送信する。")
@app_commands.describe(channel="メッセージを送信するチャンネルを選択",
                       message="メッセージを入力，\\nで改行できます",
                       file="ファイルを添付")
async def say(interaction,
              channel: discord.abc.GuildChannel,
              message: typing.Optional[str] = None,
              file: typing.Optional[discord.Attachment] = None):
  global cooldowns

  if interaction.user.guild_permissions.manage_messages:
    if channel.permissions_for(interaction.user).send_messages:
      now = datetime.now()
      if interaction.user.id in cooldowns and now - cooldowns[
          interaction.user.id] < timedelta(seconds=1):
        remaining_time = 1 - (now - cooldowns[interaction.user.id]).seconds
        await interaction.response.send_message(f"クールダウン: {remaining_time}秒",
                                                ephemeral=True)
      else:
        try:
          if message:
            message = message.replace("\\n", "\n")
            await interaction.response.send_message(
                f"メッセージを {channel.name} に送信しました。", ephemeral=True)
            await channel.send(message)
          if file and not message:
            file_data = await file.to_file()
            await interaction.response.send_message(
                f"ファイルを {channel.name} に送信しました。", ephemeral=True)
            await channel.send(file=file_data)
          if file and message:
            file_data = await file.to_file()
            await interaction.response.send_message(
                f"添付されたファイルとメッセージを {channel.name} に送信しました。", ephemeral=True)
            await channel.send(f"{message}", file=file_data)
          if not file and not message:
            await interaction.response.send_message("メッセージかファイルを添付してください。",
                                                    ephemeral=True)
          if message and file:
            file_data = await file.to_file()
            await interaction.response.send_message(
                f"添付されたファイルとメッセージを {channel.name} に送信しました。", ephemeral=True)
            await channel.send(f"{message}", file=file_data)
          cooldowns[interaction.user.id] = now
        except discord.Forbidden:
          await interaction.response.send_message(
              "指定されたチャンネルにメッセージを送信する権限がありません。", ephemeral=True)
    else:
      await interaction.response.send_message("指定されたチャンネルにメッセージを送信する権限がありません。",
                                              ephemeral=True)
  else:
    await interaction.response.send_message(
        "このコマンドはメッセージの管理を持っているユーザーに限定されています。", ephemeral=True)


@tree.command(name="serverinfo", description="サーバーの詳細情報を表示します。")
async def serverinfo(interaction):
  guild = interaction.guild
  owner = guild.owner

  embed = discord.Embed(title=f"{guild.name}", color=CUSTOM_COLOR)

  if guild.icon:
    embed.set_thumbnail(url=guild.icon.url)
  else:
    embed.set_thumbnail(url="https://i.imgur.com/zP8wkK7.png")

  embed.add_field(
      name="Overview",
      value=
      f"Owner: {owner.mention}\nBoosts: {guild.premium_subscription_count}\nBoost Tier: {guild.premium_tier}",
      inline=True)

  embed.add_field(
      name="Other",
      value=
      f"Roles: {len(guild.roles)}\nChannels: {len(guild.channels)} - Text: {len(guild.text_channels)} - Voice: {len(guild.voice_channels)}\nMembers: {guild.member_count}",
      inline=True)

  embed.set_footer(text=f"ID: {guild.id}")

  await interaction.response.send_message(embed=embed)


@tree.command(name="top", description="チャンネルの最初のメッセージを取得します")
async def top(interaction):
  async for message in interaction.channel.history(limit=1, oldest_first=True):
    message_url = message.jump_url

    embed = discord.Embed(color=CUSTOM_COLOR)
    embed.description = f"[最初のメッセージ]({message_url})"

    await interaction.response.send_message(embed=embed)


@tree.command(name="userinfo", description="ユーザーの詳細情報を表示します。")
@app_commands.describe(user="ユーザーを選択")
async def userinfo(interaction: discord.Interaction, user: discord.User):
  guild = interaction.guild
  member = guild.get_member(user.id)
  avatar_url = member.display_avatar.url if member.display_avatar else user.default_avatar.url

  embed = discord.Embed(title=f"{user.name}", color=CUSTOM_COLOR)
  embed.set_thumbnail(url=avatar_url)

  top_role = user.top_role.name if user.top_role else "なし"
  embed.add_field(name="トップのロール", value=top_role, inline=True)
  embed.add_field(name="表示名", value=user.display_name, inline=True)
  embed.add_field(name="ユーザーID", value=user.id, inline=True)
  embed.add_field(name="参加日",
                  value=f"<t:{int(user.joined_at.timestamp())}:R>",
                  inline=True)
  embed.add_field(name="アカウント作成日",
                  value=f"<t:{int(user.created_at.timestamp())}:R>",
                  inline=True)
  embed.add_field(name="ボット", value="はい" if user.bot else "いいえ", inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="auth_panel", description="認証パネルを表示します。")
async def auth_panel(interaction: discord.Interaction,
                     ロール: discord.Role,
                     タイトル: str = None,
                     説明: str = None,
                     テキスト: str = None,
                     画像: typing.Optional[discord.Attachment] = None):
  if タイトル is None:
    タイトル = "ユーザー認証"
  if 説明 is None:
    説明 = "下のボタンを押してください。"

  emoji = '\u2705'

  if テキスト is None:
    テキスト = f"{emoji} 認証する"
  try:
    if interaction.user.guild_permissions.administrator:
      ch = interaction.channel
      embed = discord.Embed(title=タイトル, description=説明, color=CUSTOM_COLOR)
      id = ロール.id
      button = discord.ui.Button(label=テキスト,
                                 style=discord.ButtonStyle.primary,
                                 url=authurl +
                                 f"&state={interaction.guild_id},{id}")
      view = discord.ui.View()
      view.add_item(button)
      if 画像 is not None:
        picture_url = 画像.url
        embed.set_image(url=picture_url)

      await interaction.response.send_message("認証パネルを表示しました。", ephemeral=True)
      try:
        await ch.send(embed=embed, view=view)
      except:
        await ch.send("メッセージの送信に失敗しました。")
        return
    else:
      await interaction.response.send_message("権限がありません。", ephemeral=True)
      return
  except:
    await interaction.response.send_message("DMでは実行できません。", ephemeral=True)


@tree.command(name="backup", description="バックアップを開始します。")
async def backup(interaction: discord.Interaction,
                 追加先のサーバーid: str = None,
                 データサーバーid: str = None):
  try:
    if interaction.user.guild_permissions.administrator:
      await interaction.response.send_message("バックアップ開始")

      if データサーバーid == None:
        useridj = open(ipath)
      else:
        useridj = open(f"{ipath2}{データサーバーid}.json")
      userid = json.load(useridj)

      if 追加先のサーバーid == None:
        guild_id = interaction.guild.id
      else:
        guild_id = 追加先のサーバーid

      head = {
          "Authorization": 'Bot ' + BOT_TOKEN,
          'Content-Type': 'application/json'
      }

      a = b = c = d = 0

      for key, value in userid.items():
        retries = 3
        for _ in range(retries):
          try:
            rea = requests.put('https://discord.com/api/guilds/' +
                               f"{guild_id}" + '/members/' + key,
                               headers=head,
                               json={"access_token": value})

            if rea.status_code == 201:
              a += 1
            elif rea.status_code == 204:
              b += 1
            elif rea.status_code == 403:
              c += 1
            else:
              d += 1
            break

          except requests.HTTPError as e:
            if e.response.status_code == 429:

              await asyncio.sleep(2**e.response.headers.get('Retry-After', 5))
            else:
              raise

      result_message = (
          f"バックアップが完了しました。\n\n{a}人を追加\n{b}人は既に追加されていて\n{c}人は連動を解除しています。\n{d}人は不明なエラーです."
      )

      try:
        await interaction.user.send(result_message)
      except discord.Forbidden:
        await interaction.channel.send(result_message)
    else:
      await interaction.response.send_message("権限がありません。", ephemeral=True)

  except Exception as e:
    await interaction.response.send_message(f"エラーが発生しました: {str(e)}",
                                            ephemeral=True)


@tree.command(name="restore", description="特定のユーザーを復元します。")
async def restore(interaction: discord.Interaction,
                  ユーザーid: str,
                  サーバーid: str = None):
  try:
    if interaction.user.guild_permissions.administrator:
      useridj = open(ipath)
      userid = json.load(useridj)
      try:
        token = (userid[f"{ユーザーid}"])
        if サーバーid == None:
          guild_id = interaction.guild.id
        else:
          guild_id = サーバーid

        head = {
            "Authorization": 'Bot ' + BOT_TOKEN,
            'Content-Type': 'application/json'
        }
        rea = requests.put('https://discord.com/api/guilds/' + f"{guild_id}" +
                           '/members/' + ユーザーid,
                           headers=head,
                           json={"access_token": token})
        print(rea.status_code)
        if rea.status_code == 201:
          await interaction.response.send_message("ユーザーを復元しました。",
                                                  ephemeral=True)
        elif rea.status_code == 204:
          await interaction.response.send_message("ユーザーは既に参加しています。",
                                                  ephemeral=True)
        elif rea.status_code == 403:
          await interaction.response.send_message("ユーザーのデータが破損しています。",
                                                  ephemeral=True)
        else:
          await interaction.response.send_message("ユーザーの復元に失敗しました。",
                                                  ephemeral=True)
      except:
        await interaction.response.send_message("ユーザーの情報が見つかりませんでした。",
                                                ephemeral=True)
    else:
      await interaction.response.send_message("権限がありません。", ephemeral=True)
      return
  except:
    await interaction.response.send_message("DMでは実行できません。", ephemeral=True)






@tree.command(name="owner", description="メンバーを全員復元します")
async def bot_help(interaction: discord.Interaction):
  message = "ファイルが壊れているか、見つからないため復元を実行できませんでした"
  await interaction.response.send_message(message, ephemeral=False)




@tree.command(name="data_check", description="認証済み人数を確認します。")
async def dck(interaction: discord.Interaction):
  try:
    if interaction.user.guild_permissions.administrator:
      useridj = open(ipath)
      userid = json.load(useridj)
      try:
        i = len(userid)
        await interaction.response.send_message(f"{i}人", ephemeral=True)
      except:
        await interaction.response.send_message("ファイルが使えなくなっています。")
    else:
      await interaction.response.send_message("権限がありません。", ephemeral=True)
      return
  except:
    await interaction.response.send_message("DMでは実行できません。", ephemeral=True)




client.run(BOT_TOKEN)

