import * as React from "react";
import { OrderedItem as OrderedItemType } from "../types/ApiPostTypes";
import { IExtraType } from "../types/ExtrasGroup";

const DishContext = React.createContext<
  [OrderedItemType[], (dishes: OrderedItemType[]) => void]
>([
  [
    {
      dishId: 0,
      dishName: "foo",
      orderedExtras: [],
      totalCost: 0,
    },
  ],
  () => {},
]);

export const DishProvider = DishContext.Provider;

export default DishContext;
