<template>
  <div>
    <b-row>
      <slot name="header" />
    </b-row>
    <b-row>
      <slot name="body" />
    </b-row>
  </div>
</template>

<script>
export default {
  name: "MainLayout",
};
</script>