import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { StatisticsData } from '../types/data';
import { ChartBar } from 'lucide-react';

interface StatisticsProps {
  data: StatisticsData[];
}

export function Statistics({ data }: StatisticsProps) {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center gap-2 mb-6">
        <ChartBar className="w-6 h-6 text-green-600" />
        <h2 className="text-2xl font-bold text-gray-800">Estadísticas</h2>
      </div>

      <div className="overflow-x-auto">
        <BarChart width={600} height={300} data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="field" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="count" fill="#4CAF50" />
        </BarChart>
      </div>
    </div>
  );
}