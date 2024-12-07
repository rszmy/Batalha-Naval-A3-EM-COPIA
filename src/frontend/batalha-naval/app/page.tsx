"use client";

import { useState, useEffect } from "react";

const token = '123'

export default function Fila() {
  const [nomeJogador, setNomeJogador] = useState("");
  const [jogadoresNaFila, setJogadoresNaFila] = useState([]);
  const [mensagem, setMensagem] = useState("");

  // Função para buscar jogadores na fila
  const fetchJogadoresNaFila = async () => {
    try {
      const response = await fetch("http://localhost:8000/fila/jogadores_na_fila");
      if (!response.ok) {
        throw new Error("Erro ao buscar jogadores na fila");
      }
      const data = await response.json();
      setJogadoresNaFila(data);
    } catch (error) {
      console.error("Erro ao buscar jogadores na fila:", error);
    }
  };

  // Função para entrar na fila
  const entrarNaFila = async () => {
    try {
      const response = await fetch(`http://localhost:8000/fila/entrar/${nomeJogador}/?token=${token}`, {
        method: "POST",
      });
      const data = await response.json();
      setMensagem(data.message || "Você entrou na fila!");
      fetchJogadoresNaFila(); // Atualizar a lista
    } catch (error) {
      setMensagem("Erro ao entrar na fila. Verifique os dados.");
      console.error("Erro:", error);
    }
  };

  // Função para checar o status da partida
  const checarStatusPartida = async () => {
    try {
      const response = await fetch(`http://localhost:8000/fila/checagem/${nomeJogador}?token=${token}`);
      const data = await response.json();
      setMensagem(data.message || "Você não está em uma partida.");
    } catch (error) {
      setMensagem("Erro ao checar o status da partida.");
      console.error("Erro:", error);
    }
  };

  // Atualizar a lista de jogadores ao carregar a página
  useEffect(() => {
    fetchJogadoresNaFila();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Gerenciamento da Fila</h1>

      {/* Formulário para entrar na fila */}
      <div style={{ marginBottom: "20px" }}>
        <h2>Entrar na Fila</h2>
        <input
          type="text"
          placeholder="Nome do Jogador"
          value={nomeJogador}
          onChange={(e) => setNomeJogador(e.target.value)}
          style={{ marginRight: "10px" }}
        />
        <button onClick={entrarNaFila}>Entrar</button>
      </div>

      {/* Mensagem de feedback */}
      {mensagem && <p>{mensagem}</p>}

      {/* Botão para checar o status da partida */}
      <div style={{ marginBottom: "20px" }}>
        <h2>Checar Status da Partida</h2>
        <button onClick={checarStatusPartida}>Checar</button>
      </div>

      {/* Lista de jogadores na fila */}
      <div>
        <h2>Jogadores na Fila</h2>
        {jogadoresNaFila.length > 0 ? (
          <ul>
            {jogadoresNaFila.map((jogador, index) => (
              <li key={index}>{jogador.nome}</li>
            ))}
          </ul>
        ) : (
          <p>Nenhum jogador na fila.</p>
        )}
      </div>
    </div>
  );
}