import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

stock_actual = 40

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def tienda(ctx):
    embed = discord.Embed(
        title="🛒 BLOCK SPIN SHOP",
        description="🔥 Bienvenido a la tienda oficial 🔥",
        color=0x5865F2
    )

    embed.add_field(
        name="📦 Paquetes Disponibles",
        value=(
            "🔥 1 Cuenta → $100 MXN\n"
            "🔥 3 Cuentas → $270 MXN\n"
            "🔥 5 Cuentas → $400 MXN"
        ),
        inline=False
    )

    embed.add_field(
        name="💳 Método de Pago",
        value="OXXO\nTransferencia",
        inline=True
    )

    embed.add_field(
        name="⚡ Entrega",
        value="Rápida",
        inline=True
    )

    embed.add_field(
        name="🛡️ Garantía",
        value="Soporte disponible",
        inline=False
    )

    embed.set_footer(text="Block Spin Shop • 24/7")

    await ctx.send(embed=embed)

@bot.command()
async def precios(ctx):
    embed = discord.Embed(
        title="💰 LISTA DE PRECIOS",
        color=0x57F287
    )

    embed.add_field(name="🔥 1 Cuenta", value="$100 MXN", inline=False)
    embed.add_field(name="🔥 3 Cuentas", value="$270 MXN", inline=False)
    embed.add_field(name="🔥 5 Cuentas", value="$400 MXN", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def stock(ctx):
    global stock_actual

    embed = discord.Embed(
        title="📦 STOCK DISPONIBLE",
        description=f"Actualmente tenemos **{stock_actual}** cuentas disponibles.",
        color=0xFEE75C
    )

    await ctx.send(embed=embed)

@bot.command()
async def comprar(ctx):
    embed = discord.Embed(
        title="💳 INFORMACIÓN DE COMPRA",
        description="Para comprar abre un ticket o contacta a un administrador.",
        color=0xED4245
    )

    embed.add_field(
        name="Métodos de Pago",
        value="OXXO\nTransferencia",
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def restock(ctx, cantidad: int):
    global stock_actual

    stock_actual += cantidad

    embed = discord.Embed(
        title="🚨 RESTOCK ALERT 🚨",
        description="Nuevo inventario agregado",
        color=0x57F287
    )

    embed.add_field(
        name="📦 Cantidad Agregada",
        value=str(cantidad),
        inline=True
    )

    embed.add_field(
        name="📊 Stock Actual",
        value=str(stock_actual),
        inline=True
    )

    await ctx.send("@everyone")
    await ctx.send(embed=embed)

bot.run(TOKEN)
