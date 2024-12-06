import React, { useState } from 'react';
import { PredictionForm } from './components/PredictionForm';
import { Statistics } from './components/Statistics';
import { PredictionInput, StatisticsData } from './types/data';

function App() {
  const [predictionResult, setPredictionResult] = useState<string | null>(null);
  const [statisticsData, setStatisticsData] = useState<StatisticsData[]>([]);

  const handlePredict = (input: PredictionInput) => {
    // Here you would normally make an API call to your ML model
    // For now, we'll just simulate a prediction
    setPredictionResult('Resultado de la predicción: SÍ COBRARÁ (95% de probabilidad)');
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-gray-900">
            Sistema de Predicción de Beneficios
          </h1>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div>
            <PredictionForm onPredict={handlePredict} />
            {predictionResult && (
              <div className="mt-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded-lg">
                {predictionResult}
              </div>
            )}
          </div>
          
          <div>
            <Statistics data={statisticsData} />
          </div>
        </div>
      </main>

      <footer className="bg-white mt-8">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 text-center text-gray-600">
          <p>Desarrollado por Rubén Galaz y Francisco Becker con apoyo de ChatGPT de OpenAI</p>
        </div>
      </footer>
    </div>
  );
}

export default App;