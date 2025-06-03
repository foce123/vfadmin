<template>
  <AppPage>
    <h1>应用环境</h1>
    <!-- 这里可以添加应用环境列表的表格组件 -->
    <CrudTable>
      <template #query>
        <QueryBar>
          <QueryBarItem>
            <NInput
              v-model:value="searchKeyword"
              placeholder="请输入应用环境名称"
              @keypress.enter="$table?.handleSearch()"
            />
          </QueryBarItem>
        </QueryBar>
      </template>
    </CrudTable>

    <!-- 新增/编辑 应用环境弹窗 -->
    <CrudModal
      v-model:visible="modalVisible"
      :title="modalTitle"
      :loading="modalLoading"
      @save="handleSave"
    >
      <NForm
        ref="modalFormRef"
        label-placement="left"
        label-align="left"
        :label-width="80"
        :model="modalForm"
        :rules="envRules"
      >
        <NFormItem label="应用环境名称" path="name">
          <NInput v-model:value="modalForm.name" clearable placeholder="请输入应用环境名称" />
        </NFormItem>
        <NFormItem label="应用环境描述" path="desc">
          <NInput v-model:value="modalForm.desc" type="textarea" clearable />
        </NFormItem>
      </NForm>
    </CrudModal>
  </AppPage>
</template>

<script setup>
import { ref } from 'vue';

// 搜索关键词
const searchKeyword = ref('');
// 弹窗是否可见
const modalVisible = ref(false);
// 弹窗标题
const modalTitle = ref('');
// 弹窗加载状态
const modalLoading = ref(false);
// 弹窗表单引用
const modalFormRef = ref(null);
// 弹窗表单数据
const modalForm = ref({
  name: '',
  desc: ''
});
// 应用环境校验规则
const envRules = ref({
  name: [
    { required: true, message: '请输入应用环境名称', trigger: 'blur' }
  ],
  desc: [
    { required: true, message: '请输入应用环境描述', trigger: 'blur' }
  ]
});

// 保存处理函数
const handleSave = () => {
  // 这里可以添加保存逻辑
  console.log('保存应用环境数据:', modalForm.value);
  modalVisible.value = false;
};
</script>
