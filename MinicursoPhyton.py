import pandas as pd
import win32com.client as win32



tabela_vendas = pd.read_excel('Vendas.xlsx')

# 6 - Visualização de dados no pandas
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# 7 - Faturamento por loja
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

#8 - Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()

#9 - ticket medio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:'Ticket Médio'})#mudando o nome da coluna,que não tinha
print(ticket_medio)

#10 - envia email com relatório

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'leina.caroline@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>
<p>Segue o relatório de vendas por cada loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}

<p>Quantidade vendida:</p>
{quantidade.to_html()}

<p>Ticket médio dos produtos em cada Loja</p>
{ticket_medio.to_html(formatters={'Ticket Médio':'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.</p>
<p>Leina</p>
 


'''
mail.Send()
print('Email enviado')