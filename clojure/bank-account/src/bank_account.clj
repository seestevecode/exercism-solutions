(ns bank-account)

(defn open-account [] (atom 0))

(defn close-account [account] (reset! account nil))

(defn get-balance [account] (deref account))

(defn update-balance [account increase] (swap! account + increase))
