<template v>
  <form class="box container mt-6 p-4 is-rounded" @load="loadData">
    <h2 class="title">Configuration</h2>
    <hr />
    <div class="control field">
      <label class="label">Days:</label>
      <label class="checkbox mr-3"
        >Mon
        <input id="day0" ref="day0" type="checkbox" v-model="day0" />
      </label>
      <label class="checkbox mx-3"
        >Tue
        <input id="day1" ref="day1" type="checkbox" v-model="day1" />
      </label>
      <label class="checkbox mx-3"
        >Wed
        <input id="day2" ref="day2" type="checkbox" v-model="day2"/>
      </label>
      <label class="checkbox mx-3"
        >Thu
        <input id="day3" ref="day3" type="checkbox" v-model="day3"/>
      </label>
      <label class="checkbox mx-3"
        >Fri
        <input id="day4" ref="day4" type="checkbox" v-model="day4"/>
      </label>
      <label class="checkbox mx-3"
        >Sat
        <input id="day5" ref="day5" type="checkbox" v-model="day5"/>
      </label>
      <label class="checkbox ml-3"
        >Sun
        <input id="day6" ref="day6" type="checkbox" v-model="day6"/>
      </label>
    </div>
    <div class="columns is-mobile is-centered">
      <div class="column is-half">
        <label class="label">Hour:</label>
        <input
          id="hour"
          ref="hour"
          class="input is-rounded"
          type="time"
          placeholder="hour of the day"
          v-model="hour"
        />
      </div>
      <div class="column is-half">
        <label class="label">Time:</label>
        <input
          id="time"
          ref="time"
          class="input is-rounded"
          type="number"
          placeholder="time in minutes"
          v-model="time"
        />
      </div>
    </div>
    <button
      @click.prevent="updateDB"
      class="button is-danger is-fullwidth is-rounded mt-4"
    >
      Save Config
    </button>
  </form>
</template>
<script>
import app from "@/firebase/init";
var db = app.database();
var ref = db.ref("config");

var values = null;
ref.on("value", (snapshot) => {
  const data = snapshot.val();
        values = data;
        console.log(values);})

export default {
  data() {
    return {
      day0: values['days'][0],
      day1: values['days'][1],
      day2: values['days'][2],
      day3: values['days'][3],
      day4: values['days'][4],
      day5: values['days'][5],
      day6: values['days'][6],
      hour: values['hour'],
      time: values['time']
    };
  },
  name: "Config",
  methods: {
    updateDB() {
      var daysChecked = [
        this.$refs.day0.checked,
        this.$refs.day1.checked,
        this.$refs.day2.checked,
        this.$refs.day3.checked,
        this.$refs.day4.checked,
        this.$refs.day5.checked,
        this.$refs.day6.checked,
      ];
      var data = {
        days: daysChecked,
        hour: this.$refs.hour.value,
        time: this.$refs.time.value,
      };
      console.log(data);
      ref.set(data);
    },
  },
};
</script>