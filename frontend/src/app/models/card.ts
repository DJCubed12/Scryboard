export enum MatZone {
  BATTLEFIELD = 'B',
  COMMAND = 'C',
  LIBRARY = 'L',
  GRAVEYARD = 'G',
  EXILE = 'E',
  NOT_PRESENT = 'N',
}

export interface Card {
  rfid: string;
  mat_id: string;
  api_id: string | null;
  is_face_up: boolean;
  front_image: string | null;
  back_image: string | null;
  zone: MatZone;
}

export interface PairData {
  api_id: string;
  front_image: string;
  back_image: string | null;
}
