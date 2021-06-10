import * as React from "react";
import { View, ActivityIndicator } from "react-native";
import UserHeader from "../components/UserHeader";
import { User as UserType } from "../types/ApiResponseTypes";
import UserContext from "../contexts/UserContext";

const UserScreen: React.FunctionComponent = () => {
  const [userData, setUserData] = React.useState({
    id: 0,
    username: "example",
    first_name: "John",
    last_name: "Doe",
    address: "",
    account_type: 1,
  });
  const [session, setSession] = React.useContext(UserContext);
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect(() => {
    const requestData = async () => {
      const res = await fetch(
        `https://glove-backend.herokuapp.com/users/auth/user/`,
        {
          headers: {
            Authorization: `Bearer ${session.token.access_token}`,
          },
        }
      );
      if (res.ok) {
        const json = (await res.json()) as UserType;
        setUserData(json);
        setIsLoading(false);
      }
    };
    void requestData();
  }, [session]);

  return isLoading ? (
    <View>
      <ActivityIndicator size="large" color="#fff" />
    </View>
  ) : (
    <UserHeader user={userData} setUserData={setUserData} />
  );
};

export default UserScreen;
