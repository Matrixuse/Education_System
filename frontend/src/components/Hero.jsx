import React from 'react';
import './Hero.css';

export default function Hero() {
  return (
    <header className="hero">
      <h2 className="hero-title">
        Multi-Agent<br />
        <span className="gradient-text">Madarchod System</span>
      </h2>
      <p className="hero-sub">
        A <strong>Researcher</strong> sources the best
        learning materials, then <br />A <strong>Writer</strong> crafts your personalised study guide.
      </p>
    </header>
  );
}