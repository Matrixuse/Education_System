import React, { useState } from 'react';
import Hero from './components/Hero';
import InputForm from './components/InputForm';
import StickyQuickInput from './components/StickyQuickInput';
import AgentPipeline from './components/AgentPipeline';
import StudyGuide from './components/StudyGuide';
import ChatTranscript from './components/ChatTranscript';
import ThemeToggle from './components/ThemeToggle';
import './App.css';

export default function App() {
  const [phase, setPhase] = useState('idle'); // idle | running | done | error
  const [agentStatus, setAgentStatus] = useState({ researcher: 'idle', writer: 'idle' });
  const [result, setResult] = useState(null);
  const [messages, setMessages] = useState([]);
  const [error, setError] = useState('');

  const handleGenerate = async ({ topic, depth = 'intermediate', model = 'llama-3.3-70b-versatile', clearHistory = false }) => {
    setMessages(prev => clearHistory ? [{ role: 'user', content: topic }] : [...prev, { role: 'user', content: topic }]);
    setPhase('running');
    setResult(null);
    setError('');
    setAgentStatus({ researcher: 'running', writer: 'idle' });

    try {
      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic, depth, model }),
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || 'Server error');
      }

      const data = await response.json();
      setResult(data);
      setMessages(prev => [...prev, { role: 'assistant', content: `Generated a study guide for "${data.topic}".` }]);
      setAgentStatus({ researcher: 'done', writer: 'done' });
      setPhase('done');
    } catch (e) {
      setError(e.message);
      setPhase('error');
      setAgentStatus({ researcher: 'idle', writer: 'idle' });
    }
  };

  const handleReset = () => {
    setPhase('idle');
    setResult(null);
    setMessages([]);
    setError('');
    setAgentStatus({ researcher: 'idle', writer: 'idle' });
  };

  return (
    <div className="app">
      <div className="top-bar">
        <button className="btn-new header-new-guide" onClick={handleReset}>+ New Guide</button>
        <ThemeToggle />
      </div>
      <div className="bg-orbs">
        <div className="orb orb-1" />
        <div className="orb orb-2" />
        <div className="orb orb-3" />
      </div>

      <div className="content">
        <Hero />

        {phase === 'idle' && (
          <InputForm
            onGenerate={handleGenerate}
            disabled={phase === 'running'}
          />
        )}

        {(phase === 'running' || phase === 'done') && (
          <AgentPipeline status={agentStatus} phase={phase} />
        )}

        {phase === 'error' && (
          <div className="error-box">
            <span className="error-icon">⚠️</span>
            <p>{error}</p>
            <button className="btn-ghost" onClick={handleReset}>Try Again</button>
          </div>
        )}

        {messages.length > 0 && <ChatTranscript messages={messages} />}

        {phase === 'done' && result && (
          <StudyGuide result={result} onReset={handleReset} />
        )}
      </div>

      {phase === 'done' && (
        <StickyQuickInput
          onGenerate={handleGenerate}
          disabled={phase === 'running'}
        />
      )}
    </div>
  );
}