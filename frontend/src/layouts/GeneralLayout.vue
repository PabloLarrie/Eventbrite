<template>
  <b-container>
    <b-row>
      <slot name="generalBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "GeneralLayout",
};
</script>