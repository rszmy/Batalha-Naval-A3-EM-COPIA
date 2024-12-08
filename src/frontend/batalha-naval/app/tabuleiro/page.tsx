'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const [tabuleiros, setTabuleiros] = useState<string[][] | null>(null);
  const [loading, setLoading] = useState(true);
  const [nomeJogador, setNomeJogador] = useState<string | undefined>(undefined);
  const [inputs, setInputs] = useState({
    embarcacao: '',
    coordX: '',
    coordY: '',
    orientacao: '',
  });

  const router = useRouter();
  const [isClient, setIsClient] = useState(false);

  const token = '123'
  const id = 1

  const cor = {
    '1' : '#191970',
    '2' : '#00008B',
    '3' : '#1E90FF',
    '4' : '#A9A9A9',
    'default' : '#40E0D0',
  };
  
  useEffect(() => {
    setIsClient(true);
  }, []);

  useEffect(() => {
    if (isClient) {
      const storedNomeJogador = localStorage.getItem('nomeJogador');
      if (storedNomeJogador) {
        setNomeJogador(storedNomeJogador);
      }
      else{
        router.push(`/`)
      }
      }
      }, [isClient, router]);

  useEffect(() => {
    if (!nomeJogador) return; 

    const fetchTabuleiros = async () => {
      try {
        const url = `http://127.0.0.1:8000/partida/tabuleiro/${id}/${nomeJogador}/?token=${token}`;
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Erro ao buscar os tabuleiros');
        }
        const data: string[][] = await response.json();

        // Transforma cada linha (string) em um array de caracteres
        const tabuleirosProcessados = data.map(tabuleiro =>
          tabuleiro.map(linha => linha.split(''))
        );

        setTabuleiros(tabuleirosProcessados);
      } catch (error) {
        console.error('Erro:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchTabuleiros();
  }, [id, nomeJogador]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setInputs(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async () => {
    const { embarcacao, coordX, coordY, orientacao } = inputs;
    try {
      const url = `http://127.0.0.1:8000/partida/tabuleiro/peças/${id}/${nomeJogador}/${embarcacao}/${coordX}/${coordY}/${orientacao}/?token=${token}`;
      const response = await fetch(url, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (!response.ok) {
        throw new Error('Erro ao enviar os dados para a API');
      }
            const updatedResponse = await fetch(
        `http://127.0.0.1:8000/partida/tabuleiro/${id}/${nomeJogador}/?token=${token}`
      );
      const updatedData: string[][] = await updatedResponse.json();
      const tabuleirosProcessados = updatedData.map(tabuleiro =>
        tabuleiro.map(linha => linha.split(''))
      );
      setTabuleiros(tabuleirosProcessados);
    } catch (error) {
      console.error('Erro:', error);
    }
  };

  if (loading) {
    return <div>Carregando...</div>;
  }

  if (!tabuleiros || tabuleiros.length < 2) {
    return <div>Erro ao carregar os tabuleiros.</div>;
  }

  const renderizarTabuleiro = (tabuleiro: string[][]) => {
    const letras = ['A', 'B', 'C', 'D', 'E'];

    return (
      <div style={{ display: 'inline-block' }}>
        {/* Rótulos horizontais (números) */}
        <div style={{ display: 'flex', marginBottom: '5px' }}>
          {/* Espaço vazio no canto superior esquerdo */}
          <div style={{ width: '35px' }}></div>
          {['1', '2', '3', '4', '5'].map((numero, i) => (
            <div
              key={i}
              style={{
                width: '53px',
                height: '30px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 'bold',
              }}
            >
              {numero}
            </div>
          ))}
        </div>

        {/* Tabuleiro com rótulos verticais (letras) */}
        {tabuleiro.map((linha, i) => (
          <div key={i} style={{ display: 'flex' }}>
            {/* Número na lateral esquerda */}
            <div
              style={{
                width: '30px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 'bold',
              }}
            >
              {letras[i]}
            </div>
            {/* Células do tabuleiro */}
            {linha.map((celula, j) => (
              <div
                key={`${i}-${j}`}
                style={{
                  width: '50px',
                  height: '50px',
                  border: '1px solid black',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  backgroundColor: cor[celula] || cor.default,
                  color: cor[celula] ? 'white' : 'white',
                  margin: '1px'
                }}
              >
                {celula}
              </div>
            ))}
          </div>
        ))}
      </div>
    );
  };

  return (
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '20px' }}>
    <div style={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
        <div>
          <h2>Meu Tabuleiro</h2>
          {renderizarTabuleiro(tabuleiros[0])}
        </div>
        <div>
          <h2>Tabuleiro do Inimigo</h2>
          {renderizarTabuleiro(tabuleiros[1])}
        </div>
      </div>

      <div style={{ marginTop: '20px', textAlign: 'center' }}>
        <h2>Coloque as embarcações</h2>
        {['embarcacao', 'coordX', 'coordY', 'orientacao'].map((field) => (
        <div key={field} style={{ marginBottom: '10px' }}>
          <input
            type="text"
            name={field}
            placeholder={`Digite ${field}`}
            value={inputs[field as keyof typeof inputs]}
            onChange={handleInputChange}
            style={{ padding: '5px', width: '200px' }}
          />
      </div>
      ))}
      <button onClick={handleSubmit} style={{ padding: '10px 20px', marginTop: '10px' }}>
        Enviar
      </button>
    </div>
  </div>
  );
}