<template>
  <b-container>
    <b-row>
      <b-col>
        <slot name="table" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "TableLayout",
};
</script>