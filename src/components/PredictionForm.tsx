import React, { useState } from 'react';
import { PredictionInput } from '../types/data';
import { Brain } from 'lucide-react';

interface PredictionFormProps {
  onPredict: (input: PredictionInput) => void;
}

export function PredictionForm({ onPredict }: PredictionFormProps) {
  const [formData, setFormData] = useState<PredictionInput>({
    COMUNA: '',
    REGION: '',
    URBANIDAD: '',
    FPAGO: '',
    TIPOBENEFICIO: '',
    COBROMARZO: '',
    SEXO: '',
    ECIVIL: '',
    NACIONALIDAD: ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onPredict(formData);
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center gap-2 mb-6">
        <Brain className="w-6 h-6 text-blue-600" />
        <h2 className="text-2xl font-bold text-gray-800">Predicción de Beneficios</h2>
      </div>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Región</label>
            <select
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              value={formData.REGION}
              onChange={(e) => setFormData({ ...formData, REGION: e.target.value })}
            >
              <option value="">Seleccione región</option>
              {/* Add options dynamically */}
            </select>
          </div>
          
          {/* Add more form fields similarly */}
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors"
        >
          Realizar Predicción
        </button>
      </form>
    </div>
  );
}