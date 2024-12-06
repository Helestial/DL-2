export interface PredictionInput {
  COMUNA: string;
  REGION: string;
  URBANIDAD: string;
  FPAGO: string;
  TIPOBENEFICIO: string;
  COBROMARZO: string;
  SEXO: string;
  ECIVIL: string;
  NACIONALIDAD: string;
}

export interface StatisticsData {
  field: string;
  count: number;
}