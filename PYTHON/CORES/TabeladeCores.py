Padrão de cores ANSI.
Este são os códigos de estilo e cor que melhor funcionam no Python.
Sintaxe: '\033[ESTILO;FG;BGm'.
EXEMPLO: \033[1;31m

#O texto deve ser inserido apos a letra 'm'.
Estilo:
- **0**: (Nome) sem cor.
- **1**: (old) Negrito.
- **4**: (Underline) Sublinhado.
- **7**: (Negative) Inverte letra e fundo.
Cor do texto (fg):
- **30**: Branco.
- **31**: Vermelho.
- **32**: Verde.
- **33**: Amarelo.
- **34**: Azul.
- **35**: Magenta.
- **36**: Cyan (azul claro).
- **37**: Cinza.
Cor de fundo (bg):
- **40**: Branco.
- **41**: Vermelho.
- **42**: Verde.
- **43**: Amarelo.
- **44**: Azul.
- **45**: Magenta.
- **46**: Cyan (azul claro).
- **47**: Cinza.
    **OBS**: Para limpar/limitar a formatação deve-se utilizar '\033[m'
    '''
