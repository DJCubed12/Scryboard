import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PairData } from 'src/app/models/card';
import { DEFAULT_CARD_BACK_URL } from 'src/constants';

@Component({
  selector: 'card-result',
  templateUrl: './card-result.component.html',
  styleUrls: ['./card-result.component.scss'],
})
export class CardResultComponent {
  @Input() card: any | null = null;
  @Output() pair = new EventEmitter<PairData>();
  public isFaceUp: boolean = true;

  public getCardImage(): string | null {
    try {
      const image_url = this.card?.image_uris?.small;
      if (image_url) {
        return image_url;
      } else if (this.isFaceUp) {
        const new_url = this.card?.card_faces[0]?.image_uris?.small;
        return new_url;
      } else {
        const new_url = this.card?.card_faces[1]?.image_uris?.small;
        return new_url;
      }
    } catch (TypeError) {
      // Card response doesn't follow normal format
      // TODO: try to get the image another way
    }
    return null;
  }

  public isDoubleSided() {
    if (this.card.card_faces) {
      return true;
    } else {
      return false;
    }
  }

  public flip() {
    this.isFaceUp = !this.isFaceUp;
  }

  public emitPairEvent() {
    if (this.isDoubleSided()) {
      this.pair.emit({
        api_id: this.card.id,
        front_image: this.card.card_faces[0].image_uris.large,
        back_image: this.card.card_faces[1].image_uris.large,
      });
    } else {
      this.pair.emit({
        api_id: this.card.id,
        front_image: this.card?.image_uris?.large,
        back_image: DEFAULT_CARD_BACK_URL,
      });
    }
  }
}
