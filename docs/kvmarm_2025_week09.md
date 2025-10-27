# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 09:21:31

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 280
- **总 Thread 数**: 33
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 28 threads (261 邮件)
- **RFC**: 1 threads (2 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 1 threads (3 邮件)
- **Other**: 2 threads (12 邮件)

---

## 📌 PATCH

共 28 个 thread

---

### Thread 1: [PATCH v2 0/4] Selftest for pKVM ownership transitions

**📧 邮件数**: 28 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 25 Feb 2025 01:53:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 pKVM 所有权转换的自测补丁（PATCH v2 0/4）。该补丁旨在增强对 pKVM 内存所有权转换的测试，确保在不同状态下的转换能够正确处理。

**原始补丁内容**：补丁包括四个部分，主要是为 pKVM 添加自测功能，检测内存所有权的合法转换。补丁的更新包括对非保护（np）客户机的支持、引入 .data 段以支持非零全局变量，以及根据之前的讨论更新了对 hyp/host 转换的断言。

**之前讨论要点**：在历史讨论中，参与者们关注了如何有效地测试 pKVM 的内存所有权转换，特别是如何处理不合法的转换情况。讨论中提到的 WARN() 机制在测试中造成了困难，因此决定去掉不必要的警告。

**本周新讨论与进展**：本周的讨论集中在补丁的具体实现上，包括对自测功能的扩展，以涵盖与非保护客户机共享页面的情况。参与者们对补丁的逻辑和实现细节进行了审查，提出了对错误代码处理的改进建议，并讨论了如何在不影响其他功能的情况下进行调试。整体来看，补丁得到了积极的反馈，并在逐步完善中。

#### 📝 邮件列表

1. **[02-25 01:53]** [PATCH v2 0/4] Selftest for pKVM ownership transitions
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-25 01:53]** [PATCH v2 1/4] KVM: arm64: Add .hyp.data section
   - 发件人: Quentin Perret <qperret@google.com>
3. **[02-25 01:53]** [PATCH v2 2/4] KVM: arm64: Don't WARN from __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
4. **[02-25 01:53]** [PATCH v2 3/4] KVM: arm64: Selftest for pKVM transitions
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-25 01:53]** [PATCH v2 4/4] KVM: arm64: Extend pKVM selftest for np-guests
   - 发件人: Quentin Perret <qperret@google.com>
6. **[02-25 18:02]** Re: [PATCH v2 2/4] KVM: arm64: Don't WARN from __pkvm_host_share_guest()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-25 19:49]** Re: [PATCH v2 2/4] KVM: arm64: Don't WARN from
 __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
8. **[02-26 14:21]** Re: [PATCH v2 2/4] KVM: arm64: Don't WARN from __pkvm_host_share_guest()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-26 14:32]** Re: [PATCH v2 3/4] KVM: arm64: Selftest for pKVM transitions
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-26 18:10]** Re: [PATCH v2 3/4] KVM: arm64: Selftest for pKVM transitions
   - 发件人: Quentin Perret <qperret@google.com>
11. **[02-26 21:55]** [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[02-26 21:55]** [PATCH v2 1/4] KVM: arm64: Factor out setting HCRX_EL2 traps into
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[02-26 21:55]** [PATCH v2 2/4] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[02-26 21:55]** [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[02-26 21:55]** [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[02-27 12:09]** Re: [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its corresponding host vcpu
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-27 04:47]** Re: [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[02-27 14:13]** Re: [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its corresponding host vcpu
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[02-27 14:13]** Re: [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[02-27 18:17]** [PATCH v2 0/4] KVM: arm64: Separate the hyp FF-A buffers init from
 the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
21. **[02-27 18:17]** [PATCH v2 1/4] KVM: arm64: Use the static initializer for the vesion lock
   - 发件人: Sebastian Ene <sebastianene@google.com>
22. **[02-27 18:17]** [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the
 ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
23. **[02-27 18:17]** [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
24. **[02-27 18:17]** [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx buffer
 to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
25. **[02-27 20:25]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
26. **[02-27 23:12]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
27. **[02-28 10:09]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the ffa header
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[02-28 19:44]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 2: [PATCH 0/7] KVM: x86: nVMX IRQ fix and VM teardown cleanups

**📧 邮件数**: 21 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 24 Feb 2025 15:55:35 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 x86 架构下的 nVMX IRQ 修复及虚拟机拆卸的清理工作。该讨论包含七个补丁（patch），主要目的是修复 nVMX 中 KVM 无法检测到待处理 IRQ 的问题，并改善虚拟机拆卸过程中的代码结构。

在历史讨论中，补丁的背景是由于 x86 的嵌套拆卸流程存在问题，导致在强制 VM-Exit 时可能出现空指针解引用或使用后释放的情况。补丁 1 解决了在释放虚拟机状态之前必须先释放 vCPU 的问题，补丁 2 则是针对 nVMX 的原始修复。

本周的新讨论中，参与者们对补丁进行了详细的审查和讨论。Sean Christopherson 提出了多个补丁的具体实现，包括在拆卸虚拟机时不再加载 vCPU、将 MMU 卸载与 vCPU 销毁结合等。此外，Yan Zhao 提出了对补丁的改进建议，讨论了如何优化 vCPU 和虚拟机状态的释放顺序，以避免潜在的内存访问错误。

最终，补丁 1 和 2 已被应用到 kvm/master 分支，其他补丁则计划在进一步测试后合并。整体讨论集中在提高 KVM 的稳定性和代码可维护性上。

#### 📝 邮件列表

1. **[02-24 15:55]** [PATCH 0/7] KVM: x86: nVMX IRQ fix and VM teardown cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[02-24 15:55]** [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[02-24 15:55]** [PATCH 2/7] KVM: nVMX: Process events on nested VM-Exit if injectable
 IRQ or NMI is pending
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[02-24 15:55]** [PATCH 3/7] KVM: Assert that a destroyed/freed vCPU is no longer visible
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[02-24 15:55]** [PATCH 4/7] KVM: x86: Don't load/put vCPU when unloading its MMU
 during teardown
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[02-24 15:55]** [PATCH 5/7] KVM: x86: Unload MMUs during vCPU destruction, not before
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[02-24 15:55]** [PATCH 6/7] KVM: x86: Fold guts of kvm_arch_sync_events() into kvm_arch_pre_destroy_vm()
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[02-24 15:55]** [PATCH 7/7] KVM: Drop kvm_arch_sync_events() now that all
 implementations are nops
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[02-25 15:07]** Re: [PATCH 3/7] KVM: Assert that a destroyed/freed vCPU is no longer
 visible
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
10. **[02-25 15:13]** Re: [PATCH 4/7] KVM: x86: Don't load/put vCPU when unloading its MMU
 during teardown
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
11. **[02-25 15:44]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
12. **[02-25 20:05]** Re: [PATCH 7/7] KVM: Drop kvm_arch_sync_events() now that all
 implementations are nops
   - 发件人: bibo mao <maobibo@loongson.cn>
13. **[02-25 06:35]** Re: [PATCH 3/7] KVM: Assert that a destroyed/freed vCPU is no longer visible
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[02-25 06:44]** Re: [PATCH 4/7] KVM: x86: Don't load/put vCPU when unloading its MMU
 during teardown
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[02-25 07:04]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[02-25 17:15]** Re: [PATCH 7/7] KVM: Drop kvm_arch_sync_events() now that all
 implementations are nops
   - 发件人: Claudio Imbrenda <imbrenda@linux.ibm.com>
17. **[02-26 00:47]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
18. **[02-25 16:27]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[02-26 15:34]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
20. **[02-26 10:18]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
21. **[02-26 19:38]** Re: [PATCH 0/7] KVM: x86: nVMX IRQ fix and VM teardown cleanups
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 3: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 20 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 18 Feb 2025 14:39:55 -0600

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构上启用分支栈采样的补丁系列（[PATCH v20 00/11]），该功能基于 ARMv9.2 架构的分支记录缓冲扩展（BRBE）。历史讨论中，Rob Herring 提到该补丁系列经过多次重构，主要集中在第11个补丁上，旨在支持在虚拟机环境中记录分支信息。

在之前的讨论中，参与者探讨了如何在 nVHE（非虚拟化高效）环境中禁用来宾的分支生成，以及在来宾进入和退出时如何管理 BRBE 状态。补丁 10 和 11 主要关注在虚拟化环境中如何处理分支记录的保存和恢复。

本周的新讨论中，参与者 Leo Yan 提出了对补丁 11 的一些关注，特别是任务迁移时如何处理分支记录的问题。他指出当前实现中，任务切换时会简单地使所有记录失效，这可能导致在上下文切换期间丢失重要的分支信息。Mark Rutland 也对此表示了关注，讨论了在事件轮换和过滤器合并时可能出现的复杂性。

整体而言，本周的讨论围绕如何优化 BRBE 的实现，以确保在多事件和多任务环境中有效记录分支信息，避免因上下文切换而导致的数据丢失。参与者们对如何处理不同事件的过滤器和记录保持一致性进行了深入探讨。

#### 📝 邮件列表

1. **[02-18 14:39]** [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[02-18 14:40]** [PATCH v20 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[02-18 14:40]** [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
4. **[02-24 10:41]** Re: [PATCH v20 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[02-24 12:25]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
6. **[02-24 06:46]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
7. **[02-24 14:03]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
8. **[02-24 16:05]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[02-24 18:03]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
10. **[02-24 19:31]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
11. **[02-25 12:01]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
12. **[02-25 12:38]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
13. **[02-25 09:35]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
14. **[02-25 17:48]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
15. **[02-25 13:04]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
16. **[02-25 19:46]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
17. **[02-25 19:58]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
18. **[02-26 13:48]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
19. **[02-26 08:26]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
20. **[03-01 07:05]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 4: [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 10:25:16 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 非特权虚拟机（np-guest）支持的阶段二大页映射的补丁系列（共9个补丁）。该补丁系列的主要目标是实现阶段二大页映射（PMD_SIZE），以便在使用 Hugetlbfs 或透明大页（THP）时，能够在阶段二中安装 PMD 级别的映射。

在历史讨论中，参与者 Vincent Donnefort 提出了补丁的初步内容，强调了在处理缓存管理操作（CMOs）时，现有的 `clean_dcache_guest_page()` 和 `invalidate_icache_guest_page()` 函数需要支持大于单页大小的参数。补丁系列的最后一个补丁则针对使用共享 PMD_SIZE fixmap 的 CMOs 进行了优化。

本周的新讨论中，Vincent Donnefort 提出了多个补丁，包括：
1. **补丁1**：修改了 `clean_dcache_guest_page()` 和 `invalidate_icache_guest_page()` 函数，以支持大于 PAGE_SIZE 的大小。
2. **补丁2**：为 `__pkvm_host_share_guest()` 添加了 `nr_pages` 参数，以支持阶段二大页映射。
3. **补丁3**：为 `__pkvm_host_unshare_guest()` 添加了 `nr_pages` 参数。
4. **补丁4**：为 `__pkvm_host_wrprotect_guest()` 添加了 `nr_pages` 参数。
5. **补丁5**：为 `__pkvm_host_test_clear_young_guest()` 添加了 `nr_pages` 参数。
6. **补丁6**：将 `pkvm_mappings` 转换为区间树，以支持大页映射。
7. **补丁7**：为 `pkvm_mapping` 结构添加了 `nr_pages` 成员，以跟踪阶段二映射的大小。
8. **补丁8**：实现了 np-guest 的阶段二大页映射。
9. **补丁9**：引入了共享 PMD_SIZE fixmap，以改善大页映射的 CMOs 性能。

讨论中还提到了一些代码的安全性和健壮性问题，确保在处理内存地址时的有效性。整体来看，这一系列补丁旨在提升 pK

#### 📝 邮件列表

1. **[02-28 10:25]** [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-28 10:25]** [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-28 10:25]** [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-28 10:25]** [PATCH 2/9] KVM: arm64: Add range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[02-28 10:25]** [PATCH 3/9] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[02-28 10:25]** [PATCH 3/9] KVM: arm64: Add range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[02-28 10:25]** [PATCH 4/9] KVM: arm64: Add a range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[02-28 10:25]** [PATCH 4/9] KVM: arm64: Add range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[02-28 10:25]** [PATCH 5/9] KVM: arm64: Add a range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[02-28 10:25]** [PATCH 5/9] KVM: arm64: Add range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[02-28 10:25]** [PATCH 6/9] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[02-28 10:25]** [PATCH 7/9] KVM: arm64: Add a range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[02-28 10:25]** [PATCH 7/9] KVM: arm64: Add range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[02-28 10:25]** [PATCH 8/9] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[02-28 10:25]** [PATCH 9/9] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[02-28 18:54]** Re: [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Quentin Perret <qperret@google.com>
17. **[02-28 19:06]** Re: [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 5: [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support

**📧 邮件数**: 17 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 25 Feb 2025 17:29:14 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是为 KVM（Kernel-based Virtual Machine）在 ARM64 架构上添加 NV GICv3 支持。Marc Zyngier 提出了一个包含 16 个补丁的系列，旨在增强 KVM 的虚拟化能力，特别是在处理 GICv3（通用中断控制器）时的性能和功能。

**原始补丁/问题内容**：
补丁的主要目标是实现对 GICv3 的支持，特别是在嵌套虚拟化环境中。补丁包括对 GICv3 相关寄存器的定义、处理和仿真，确保在虚拟化时能够正确处理中断。

**之前讨论要点**：
在历史讨论中，Marc 提到了一些补丁的演变过程，包括对寄存器默认值的修正和对不同版本的补丁进行重基。讨论中还提到了一些关键的寄存器布局和中断处理机制的改进。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在补丁的具体实现上，包括：
1. 增加了对 ICH_*_EL2 寄存器的支持，以便在嵌套虚拟化中正确处理中断。
2. 讨论了如何在 L2 到 L1 的中断注入过程中确保正确的异常处理。
3. 引入了维护中断的仿真机制，以便在 L2 运行时能够正确反映 L1 的状态。
4. 讨论了如何处理 WFI/WFE 指令的异常转发，以及在嵌套 ERET 时请求 vPE 门铃中断。

此外，Marc 还强调了在没有 GICv3 的情况下，KVM 初始化将失败，以确保虚拟化环境的兼容性和稳定性。这些补丁的最终目标是提升 KVM 在 ARM64 架构上的性能和可靠性。

#### 📝 邮件列表

1. **[02-25 17:29]** [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-25 17:29]** [PATCH v4 01/16] arm64: sysreg: Add layout for ICH_HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-25 17:29]** [PATCH v4 02/16] arm64: sysreg: Add layout for ICH_VTR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-25 17:29]** [PATCH v4 03/16] arm64: sysreg: Add layout for ICH_MISR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-25 17:29]** [PATCH v4 04/16] KVM: arm64: nv: Load timer before the GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-25 17:29]** [PATCH v4 05/16] KVM: arm64: nv: Add ICH_*_EL2 registers to vpcu_sysreg
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-25 17:29]** [PATCH v4 06/16] KVM: arm64: nv: Plumb handling of GICv3 EL2 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-25 17:29]** [PATCH v4 07/16] KVM: arm64: nv: Sanitise ICH_HCR_EL2 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-25 17:29]** [PATCH v4 08/16] KVM: arm64: nv: Nested GICv3 emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-25 17:29]** [PATCH v4 09/16] KVM: arm64: nv: Handle L2->L1 transition on interrupt injection
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-25 17:29]** [PATCH v4 10/16] KVM: arm64: nv: Add Maintenance Interrupt emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[02-25 17:29]** [PATCH v4 11/16] KVM: arm64: nv: Respect virtual HCR_EL2.TWx setting
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[02-25 17:29]** [PATCH v4 12/16] KVM: arm64: nv: Request vPE doorbell upon nested ERET to L2
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[02-25 17:29]** [PATCH v4 13/16] KVM: arm64: nv: Propagate used_lrs between L1 and L0 contexts
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[02-25 17:29]** [PATCH v4 14/16] KVM: arm64: nv: Fold GICv3 host trapping requirements into guest setup
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-25 17:29]** [PATCH v4 15/16] KVM: arm64: nv: Allow userland to set VGIC maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-25 17:29]** [PATCH v4 16/16] KVM: arm64: nv: Fail KVM init if asking for NV without GICv3
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH 0/4] mm: Rework generic PTDUMP configs

**📧 邮件数**: 16 | **👥 参与者**: 5 | **📅 开始时间**: Thu, 13 Feb 2025 09:39:30 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 Linux 内核中通用 PTDUMP 配置的重构及相关问题。历史讨论中，Anshuman Khandual 提出了一个补丁系列，旨在重命名和清理通用 PTDUMP 配置，以提高可读性和明确性。具体来说，补丁将 `GENERIC_PTDUMP` 和 `PTDUMP_CORE` 重命名为 `ARCH_HAS_PTDUMP` 和 `PTDUMP`，以消除混淆。讨论中，Christophe Leroy 和 Steven Price 对命名提出了不同看法，认为 `GENERIC_PTDUMP` 更加明确，且不应在用户可选符号中列出。

在本周的新讨论中，Christophe Leroy 继续表达对补丁命名的疑虑，并建议进行替换。Oliver Upton 则提交了一系列针对 KVM 的补丁，解决了 GICv4 vLPI 注入中的一些问题，包括确保在创建 irqbypass 映射之前恢复虚拟 ITS 的顺序。最终，Marc Zyngier 对这些补丁表示认可，Oliver Upton 也确认已将其应用到下一个版本中。

总结来说，历史讨论集中在 PTDUMP 配置的命名和清理上，而本周则转向 KVM 的具体修复和文档更新，显示出社区对内核功能的持续关注与改进。

#### 📝 邮件列表

1. **[02-13 09:39]** [PATCH 0/4] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-13 09:39]** [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-13 08:38]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
4. **[02-13 11:23]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Steven Price <steven.price@arm.com>
5. **[02-13 12:49]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
6. **[02-14 12:47]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-14 12:56]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
8. **[02-24 12:12]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
9. **[02-24 12:13]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
10. **[02-26 10:31]** [PATCH 0/4] KVM: arm64: Fixes/clarification for GICv4 vLPI injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-26 10:31]** [PATCH 1/4] KVM: arm64: vgic-v4: Only attempt vLPI mapping for actual MSIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[02-26 10:31]** [PATCH 2/4] KVM: arm64: vgic-v4: Only WARN for HW IRQ mismatch when unmapping vLPI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[02-26 10:31]** [PATCH 3/4] KVM: arm64: vgic-v4: Fall back to software irqbypass if LPI not found
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[02-26 10:31]** [PATCH 4/4] KVM: arm64: Document ordering requirements for irqbypass
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[02-26 18:58]** Re: [PATCH 0/4] KVM: arm64: Fixes/clarification for GICv4 vLPI injection
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-26 13:27]** Re: [PATCH 0/4] KVM: arm64: Fixes/clarification for GICv4 vLPI injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation

**📧 邮件数**: 14 | **👥 参与者**: 6 | **📅 开始时间**: Mon, 24 Feb 2025 15:09:38 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是取消在内存插槽创建时对 `mte_allowed` 检查的要求。

**原始补丁内容**：
该补丁旨在简化内存插槽的创建过程，允许在没有设置 `VM_MTE_ALLOWED` 标志的情况下创建内存插槽。补丁指出，之前的实现中，内存插槽会因为未设置 `VM_MTE_ALLOWED` 而被拒绝，这影响了使用 MTE（Memory Tagging Extension）与 VFIO（Virtual Function I/O）直通的能力。

**之前讨论要点**：
在历史讨论中，参与者提到，之前的实现为了避免竞争条件，限制了共享页面的 MTE 使用。随着对锁定机制的更新，允许了共享映射与 MTE 的结合，因此需要对内存插槽创建的检查进行调整。

**本周新讨论进展**：
本周的讨论中，参与者对补丁表示支持，并提出了一些细节上的改进建议。例如，Marc Zyngier 提出了关于 DMA 和 MTE 交互的疑问，并指出可能导致的内存一致性问题。Aneesh Kumar 提议在发生内存故障时提供更多信息，以帮助用户空间进行调试。此外，讨论还涉及到是否将 MTE 的使用与特定的硬件特性（如 `FEAT_MTE_PERM`）绑定，以确保 VMM（虚拟机监控程序）能够正确处理内存插槽的创建。

总体而言，补丁获得了积极反馈，但仍需进一步讨论如何在实现中平衡灵活性与安全性。

#### 📝 邮件列表

1. **[02-24 15:09]** [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[02-24 10:32]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[02-24 11:05]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[02-24 12:24]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-24 14:39]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-24 15:02]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-24 22:14]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
8. **[02-24 17:23]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-24 18:00]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[02-26 00:02]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-26 15:28]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
12. **[02-26 15:58]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
13. **[02-26 22:18]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
14. **[02-26 18:02]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 8: [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 24 Feb 2025 16:53:56 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下可写 MIDR（主实现 ID 寄存器）和 REVIDR（修订 ID 寄存器）的补丁系列（PATCH v4 0/5）。该系列补丁的主要目标是允许用户空间修改实现 ID 寄存器，以便在虚拟机中提供更灵活的 CPU 识别。

在历史讨论中，补丁系列经历了多次迭代，主要集中在如何处理这些寄存器的可写性以及如何避免破坏现有的 ABI（应用二进制接口）。之前的讨论强调了寄存器的“不可变性”，即用户空间只能看到启动 CPU 的值，而不能修改。

本周的新讨论中，Oliver Upton 提出了补丁 v4，重构了寄存器的访问方式，并引入了用户空间的参与，以使 MIDR、REVIDR 和 AIDR 寄存器可写。补丁还包括对 HCR_EL2.TID1 的无条件设置，以确保正确处理寄存器的陷阱。此外，Sebastian Ott 提供了自测代码，确保这些寄存器的写入操作在用户空间中有效，并且在 vCPU 重置时保持一致性。

Marc Zyngier 对补丁提出了一些建议，指出需要处理 AArch32 版本的 REVIDR 和 AIDR 寄存器的陷阱。整体来看，讨论围绕如何在不破坏现有功能的情况下，增强 KVM 对实现 ID 寄存器的支持，确保其在虚拟化环境中的有效性和一致性。

#### 📝 邮件列表

1. **[02-24 16:53]** [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-24 16:53]** [PATCH v4 1/5] KVM: arm64: Set HCR_EL2.TID1 unconditionally
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-24 16:53]** [PATCH v4 2/5] KVM: arm64: Maintain per-VM copy of implementation ID regs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-24 16:53]** [PATCH v4 3/5] KVM: arm64: Load VPIDR_EL2 with the VM's MIDR_EL1 value
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-24 16:54]** [PATCH v4 4/5] KVM: arm64: Allow userspace to change the implementation ID registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[02-24 16:54]** [PATCH v4 5/5] KVM: selftests: arm64: Test writes to MIDR,REVIDR,AIDR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[02-25 11:09]** Re: [PATCH v4 1/5] KVM: arm64: Set HCR_EL2.TID1 unconditionally
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-25 11:19]** Re: [PATCH v4 4/5] KVM: arm64: Allow userspace to change the implementation ID registers
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-25 13:54]** Re: [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-26 01:49]** Re: [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-27 20:39]** Re: [PATCH v4 5/5] KVM: selftests: arm64: Test writes to
 MIDR,REVIDR,AIDR
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[02-28 10:47]** Re: [PATCH v4 5/5] KVM: selftests: arm64: Test writes to
 MIDR,REVIDR,AIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
13. **[02-28 14:21]** Re: [PATCH v4 5/5] KVM: selftests: arm64: Test writes to
 MIDR,REVIDR,AIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 9: [PATCH V3 0/5] mm: Rework generic PTDUMP configs

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 26 Feb 2025 17:53:59 +0530

#### 🤖 AI 总结

本周讨论的主题是关于对 Linux 内核中通用页面转储（PTDUMP）配置的重构，涉及的补丁系列为「[PATCH V3 0/5] mm: Rework generic PTDUMP configs」。该系列补丁旨在清理和重命名 PTDUMP 相关的配置，以提高可读性和一致性。

历史讨论中，补丁的初始版本（V1 和 V2）提出了对 GENERIC_PTDUMP 的依赖性进行调整，并删除了一些不必要的配置选项。V2 中还删除了与 MMU 相关的依赖，进一步简化了配置。

在本周的新讨论中，Anshuman Khandual 提交了 V3 版本的补丁，主要包括以下更改：
1. 在 mpc885_ads_defconfig 中添加了 CONFIG_PTDUMP_DEBUGFS，并恢复了 riscv 平台对 CONFIG_ARCH_HAS_PTDUMP 的 MMU 依赖。
2. 删除了 debug.config 中的 GENERIC_PTDUMP 配置，确保只有支持该功能的平台才能启用。
3. 更新了文档，移除了不再可选的 PTDUMP 配置选项。
4. 将 DEBUG_WX 的依赖关系修改为依赖于 GENERIC_PTDUMP。
5. 将 GENERIC_PTDUMP 和 PTDUMP_CORE 重命名为 ARCH_HAS_PTDUMP 和 PTDUMP，以减少混淆。

本周讨论中，多个参与者对补丁进行了审查并给予了认可，表明补丁在社区中得到了积极的反馈。整体来看，这一系列补丁旨在提升内核配置的清晰度和可维护性。

#### 📝 邮件列表

1. **[02-26 17:53]** [PATCH V3 0/5] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-26 17:54]** [PATCH V3 1/5] configs: Drop GENERIC_PTDUMP from debug.config
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-26 17:54]** [PATCH V3 2/5] arch/powerpc: Drop GENERIC_PTDUMP from mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-26 17:54]** [PATCH V3 3/5] docs: arm64: Drop PTDUMP config options from ptdump.rst
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[02-26 17:54]** [PATCH V3 4/5] mm: Make DEBUG_WX depdendent on GENERIC_PTDUMP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[02-26 17:54]** [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-26 13:31]** Re: [PATCH V3 2/5] arch/powerpc: Drop GENERIC_PTDUMP from
 mpc885_ads_defconfig
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
8. **[02-26 13:31]** Re: [PATCH V3 4/5] mm: Make DEBUG_WX depdendent on GENERIC_PTDUMP
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
9. **[02-26 13:33]** Re: [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
10. **[02-26 19:45]** Re: [PATCH V3 3/5] docs: arm64: Drop PTDUMP config options from
 ptdump.rst
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[02-26 19:53]** Re: [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[02-27 05:36]** Re: [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 10: [PATCH 00/11] Tracefs support for pKVM

**📧 邮件数**: 12 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 24 Feb 2025 12:13:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（共11个补丁），主要由 Vincent Donnefort 提出。以下是讨论的要点：

1. **原始补丁内容**：该系列补丁旨在为 pKVM 提供 Tracefs 支持，以便在受保护模式下进行调试和性能分析。补丁引入了一个新的接口，使得 hypervisor 能够生成事件，并通过 Tracefs 用户空间接口读取这些事件。

2. **历史讨论要点**：在之前的讨论中，补丁的设计考虑了 hypervisor 与内核之间的差异，特别是在事件格式和缓冲区操作方面。补丁还解决了如何在 hypervisor 中生成事件的问题，并引入了新的 ring-buffer 结构以支持这一功能。

3. **本周的新讨论和进展**：
   - 本周的邮件中，Vincent 逐步介绍了各个补丁的具体实现，包括引入新的 ring-buffer 接口、支持时钟、添加跟踪支持、以及实现 hyp 事件的能力等。
   - 讨论中提到，Tracefs 目录下的结构与主机实例相似，便于现有用户空间工具的使用。
   - 还新增了对 hyp 事件的支持，允许在 hypervisor 中描述和发出事件，并提供了相应的测试用例以验证新接口的有效性。

总的来说，这一系列补丁的引入将显著增强 pKVM 的调试和性能分析能力，提升了对 hypervisor 行为的可观察性。

#### 📝 邮件列表

1. **[02-24 12:13]** [PATCH 00/11] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-24 12:13]** [PATCH 01/11] ring-buffer: Introduce ring-buffer remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-24 12:13]** [PATCH 02/11] ring-buffer: Expose buffer_data_page material
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-24 12:13]** [PATCH 03/11] KVM: arm64: Support unaligned fixmap in the nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[02-24 12:13]** [PATCH 04/11] KVM: arm64: Add clock support in the nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[02-24 12:13]** [PATCH 05/11] KVM: arm64: Add tracing support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[02-24 12:13]** [PATCH 06/11] KVM: arm64: Add hyp tracing to tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[02-24 12:13]** [PATCH 07/11] KVM: arm64: Add clock for hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[02-24 12:13]** [PATCH 08/11] KVM: arm64: Add raw interface for hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[02-24 12:13]** [PATCH 09/11] KVM: arm64: Add trace interface for hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[02-24 12:13]** [PATCH 10/11] KVM: arm64: Add support for hyp events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[02-24 12:13]** [PATCH 11/11] KVM: arm64: Add kselftest for tracefs hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 11: [PATCH 0/2] KVM: arm64: PSCI relay fixes

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 18:05:24 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH 0/2] KVM: arm64: PSCI relay fixes”，主要涉及对KVM在arm64架构下的PSCI中继代码的修复。

1. **原始 patch/问题的内容**：该系列补丁旨在修复PSCI中继代码中的一些初始化缺失问题，这些问题可能导致主机内核在进入PSCI的CPU_ON、CPU_SUSPEND和SYSTEM_SUSPEND冷启动点后崩溃。补丁包括初始化HCR_EL2.E2H和SCTLR_EL1的相关代码。

2. **之前的讨论要点**：在历史讨论中，问题的根源是HCR_EL2.E2H和SCTLR_EL1未被正确初始化，导致在特定情况下进入EL1时出现未知状态。参与者讨论了如何确保这些寄存器在调用PSCI时被正确设置，以避免潜在的内核崩溃。

3. **本周的新讨论、进展或结论**：本周的讨论集中在补丁的具体实现和细节上。Mark Rutland和其他参与者对补丁进行了审查，讨论了HCR_EL2.E2H的初始化逻辑和相关注释的准确性。最终，补丁被确认并应用于修复中，确保了在PSCI调用时寄存器的正确初始化。

综上所述，该邮件讨论了KVM在arm64架构下PSCI中继的初始化修复，确保了系统稳定性并解决了主机内核崩溃的问题。

#### 📝 邮件列表

1. **[02-27 18:05]** [PATCH 0/2] KVM: arm64: PSCI relay fixes
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[02-27 18:05]** [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[02-27 18:05]** [PATCH 2/2] KVM: arm64: Initialize SCTLR_EL1 in __kvm_hyp_init_cpu()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
4. **[02-28 09:29]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[02-28 09:43]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-28 09:52]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[02-28 09:56]** Re: [PATCH 2/2] KVM: arm64: Initialize SCTLR_EL1 in
 __kvm_hyp_init_cpu()
   - 发件人: Leo Yan <leo.yan@arm.com>
8. **[02-28 10:14]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Leo Yan <leo.yan@arm.com>
9. **[02-28 10:20]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-28 11:13]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Mark Rutland <mark.rutland@arm.com>
11. **[03-02 08:41]** Re: [PATCH 0/2] KVM: arm64: PSCI relay fixes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 13 Feb 2025 16:13:40 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH v7 00/45] arm64: 支持 KVM 中的 Arm CCA”，主要涉及在 KVM 中实现 Arm Confidential Compute Architecture (CCA) 的支持。

**原始 patch/问题的内容**：
该系列补丁旨在为 KVM 提供运行受保护虚拟机的能力，相关的来宾支持已在 v6.14-rc1 中合并。补丁的亮点包括将 RMM granule 大小和 PAGE_SIZE 的概念分离，使得可以在大于 4k 的主机 PAGE_SIZE 下运行。

**之前讨论的要点**：
历史讨论中，补丁的多个部分涉及到对 KVM 处理共享和私有映射的改进，增加了用于处理 mmu_notifier 事件的标志，确保 KVM 能够有效管理不同类型的内存映射。此外，还讨论了处理 Granule Protection Faults (GPFs) 的机制，以确保系统的安全性和稳定性。

**本周的新讨论、进展或结论**：
在本周的讨论中，Gavin Shan 对多个补丁进行了审查并给予了“Reviewed-by”标记，表明他对这些补丁的认可。Gavin 还指出了一些细节问题，例如在处理共享和私有映射时的冗余性，建议进一步优化。此外，他对补丁中的一些小问题提出了改进建议，整体上讨论氛围积极，进展顺利。

#### 📝 邮件列表

1. **[02-13 16:13]** [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[02-13 16:13]** [PATCH v7 01/45] KVM: Prepare for handling only shared mappings in mmu_notifier events
   - 发件人: Steven Price <steven.price@arm.com>
3. **[02-13 16:13]** [PATCH v7 02/45] kvm: arm64: Include kvm_emulate.h in kvm/arm_psci.h
   - 发件人: Steven Price <steven.price@arm.com>
4. **[02-13 16:13]** [PATCH v7 03/45] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
5. **[02-13 16:13]** [PATCH v7 04/45] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
6. **[03-03 09:36]** Re: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events
   - 发件人: Gavin Shan <gshan@redhat.com>
7. **[03-03 09:39]** Re: [PATCH v7 02/45] kvm: arm64: Include kvm_emulate.h in
 kvm/arm_psci.h
   - 发件人: Gavin Shan <gshan@redhat.com>
8. **[03-03 09:43]** Re: [PATCH v7 03/45] arm64: RME: Handle Granule Protection Faults
 (GPFs)
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[03-03 09:52]** Re: [PATCH v7 04/45] arm64: RME: Add SMC definitions for calling the
 RMM
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 13: [PATCH v1 0/3] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 14 Feb 2025 15:02:55 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 pKVM（paravirtualized KVM）中初始化 HCRX_EL2 及其他陷阱的修复。

**原始 patch/问题的内容**：
Fuad Tabba 提出的补丁（PATCH v1 1/3）旨在修复 pKVM 中 HCRX_EL2 陷阱的初始化问题，确保在系统支持该寄存器时正确设置相关陷阱。补丁中增加了 46 行代码，主要涉及对 pKVM 中虚拟机和所有 vCPU 的初始化。

**之前讨论要点**：
在历史讨论中，提到当前 pKVM 的行为是在第一个 vCPU 运行时初始化 hyp 视图，但由于 kvm_calculate_traps() 的引入，某些主机陷阱值在相应 vCPU 首次运行时才会计算，导致 pKVM 获取错误的视图。讨论中还提到需保持陷阱配置的两侧同步，以避免潜在的错误。

**本周的新讨论、进展或结论**：
本周的讨论中，Oliver Upton 对补丁表示总体认可，提出可以删除不支持的 SME 相关代码。Marc Zyngier 建议将 HCRX 的初始化部分提取到一个内联函数中，以便在 kvm_calculate_traps() 和 pkvm_vcpu_init_traps() 中调用。最终，Fuad 同意这一建议，并表示会进行相应的修改。整体来看，讨论集中在如何优化代码结构和确保功能一致性上。

#### 📝 邮件列表

1. **[02-14 15:02]** [PATCH v1 0/3] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-14 15:02]** [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-26 02:07]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-26 10:45]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-26 04:36]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[02-26 04:44]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[02-26 15:28]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-26 10:53]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[02-26 10:54]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 14: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 19 Feb 2025 14:30:28 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁（PATCH v7 09/11），旨在为 Realms 启用内存加密功能。历史讨论中，Steven Price 指出，由于 RSI 检测的延迟，调用 is_realm_world() 的时机过早，可能导致某些 Realm 客户端无法与主机共享页面。他提出了几种解决方案，其中之一是将 rodata_full 设为 Realm 客户端的要求。

在本周的新讨论中，参与者们围绕 rodata_full 的必要性展开了进一步讨论。Catalin Marinas 和 Will Deacon 认为，rodata_full 与 Realm 本身并无直接关系，但可能影响内存映射的行为。Steven Price 提出了多个选项，包括允许在禁用 rodata_full 时仍能使用页面映射的可能性，并建议引入新的编译或命令行标志来处理页面映射问题。

总体来看，本周的讨论集中在如何平衡内存映射和权限设置之间的关系，以及如何在不影响 Realm 功能的前提下优化内存管理策略。参与者们一致认为需要更深入的探讨和细致的实现，以确保补丁的有效性和稳定性。

#### 📝 邮件列表

1. **[02-19 14:30]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Steven Price <steven.price@arm.com>
2. **[02-26 19:03]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[02-27 00:23]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Will Deacon <will@kernel.org>
4. **[02-27 10:45]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Steven Price <steven.price@arm.com>
5. **[02-27 10:55]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-27 17:22]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Will Deacon <will@kernel.org>
7. **[02-27 21:21]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 15: [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 27 Feb 2025 00:33:04 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于将 pKVM 所有权状态迁移到 hyp_vmemmap 的补丁系列，共包含六个补丁。该补丁的主要目标是优化超管的状态查找，减少对页表的遍历，提高性能，并为未来的功能扩展（如 hyp 跟踪）提供便利。

在历史讨论中，补丁的背景和预期效果已经被阐述，强调了迁移后的两个主要好处：一是显著降低超管状态查找的成本，二是使超管状态与线性映射范围的存在解耦，从而简化现有代码并为未来的清理工作铺平道路。

本周的新讨论中，Quentin Perret 提出了六个补丁的具体实现，包括：
1. **补丁 1**：确保在处理启用 SVE 的客户机时，主机 SVE 状态在 EL2 S1 中被正确初始化。
2. **补丁 2**：将 PKVM_NOPAGE 的编码改为使用保留的状态，以简化后续迁移。
3. **补丁 3**：引入访问器函数以替代直接访问结构体成员，增强代码的可维护性。
4. **补丁 4**：将超管状态迁移到 hyp_vmemmap，进一步优化状态查找。
5. **补丁 5**：推迟对 EL2 stage-1 的映射，增强安全性。
6. **补丁 6**：在所有内存所有权转换中无条件交叉检查超管状态，以避免潜在问题。

这些补丁的实现被认为将显著提升系统的性能和安全性。

#### 📝 邮件列表

1. **[02-27 00:33]** [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-27 00:33]** [PATCH 1/6] KVM: arm64: Track SVE state in the hypervisor vcpu structure
   - 发件人: Quentin Perret <qperret@google.com>
3. **[02-27 00:33]** [PATCH 2/6] KVM: arm64: Use 0b11 for encoding PKVM_NOPAGE
   - 发件人: Quentin Perret <qperret@google.com>
4. **[02-27 00:33]** [PATCH 3/6] KVM: arm64: Introduce {get,set}_host_state() helpers
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-27 00:33]** [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
6. **[02-27 00:33]** [PATCH 5/6] KVM: arm64: Defer EL2 stage-1 mapping on share
   - 发件人: Quentin Perret <qperret@google.com>
7. **[02-27 00:33]** [PATCH 6/6] KVM: arm64: Unconditionally cross check hyp state
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 16: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 14:02:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构上进行虚拟机实时迁移时的错误管理的补丁（PATCH v8 0/6）。该补丁的主要目的是增强虚拟机迁移过程中对 CPU 实现的支持，确保在不同 CPU 之间迁移时能够正确处理相关的错误。

在历史讨论中，Shameer Kolothum 提出了多个补丁，主要包括：
1. 修改 `_midr_range()` 函数以支持内部读取 MIDR/REVIDR。
2. 将 `_midr_in_range_list()` 函数导出，以便后续补丁能够访问新的数据。
3. 基于实现 CPU 启用错误管理，通过超调用获取迁移目标的实现 CPU。

本周的新讨论中，Catalin Marinas 对多个补丁进行了确认（Acked-by），表示支持这些修改。这些补丁在功能上没有引入新的变化，主要是为后续的 CPU 实现支持打下基础。尽管 Catalin 提到可能存在一些潜在问题，但在缺乏更好方案的情况下，他表示接受当前的实现。

总体来看，本周的讨论主要是对之前补丁的认可，并未提出新的问题或建议。

#### 📝 邮件列表

1. **[02-21 14:02]** [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[02-21 14:02]** [PATCH v8 1/6] arm64: Modify _midr_range() functions to read MIDR/REVIDR internally
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
3. **[02-21 14:02]** [PATCH v8 4/6] =?UTF-8?q?arm64:=20Make=20=C2=A0=5Fmidr=5Fin=5Fran?= =?UTF-8?q?ge=5Flist()=20an=20exported=20function?=
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
4. **[02-21 14:02]** [PATCH v8 5/6] smccc/kvm_guest: Enable errata based on implementation CPUs
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
5. **[02-26 19:39]** Re: [PATCH v8 1/6] arm64: Modify _midr_range() functions to read
 MIDR/REVIDR internally
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-26 19:40]** Re: [PATCH v8 4/6] arm64: =?iso-8859-1?Q?M?=
 =?iso-8859-1?B?YWtlIKBfbWlkcl9pbl9yYW5nZV9saXN0KCk=?= an exported function
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[02-26 19:41]** Re: [PATCH v8 5/6] smccc/kvm_guest: Enable errata based on
 implementation CPUs
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 17: [PATCH V2 0/5] mm: Rework generic PTDUMP configs

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 17 Feb 2025 09:52:15 +0530

#### 🤖 AI 总结

本邮件线程讨论了关于 Linux 内核中通用 PTDUMP 配置的重构，主要涉及一系列补丁（patch）。原始补丁由 Anshuman Khandual 提出，包含五个部分，旨在通过基本清理后重命名通用 PTDUMP 配置，以提高可读性和清晰度。这些补丁已在 arm64 平台上测试，并且可以在其他平台上构建。

在历史讨论中，Anshuman 提出了几个补丁，包括删除 PowerPC 架构中不必要的 GENERIC_PTDUMP 配置，以及重命名配置以消除混淆。讨论中提到，现有的配置名称在平台特性订阅和功能启用之间没有明确区分，因此建议将其重命名为 ARCH_HAS_PTDUMP 和 PTDUMP。

在本周的新讨论中，Christophe Leroy 对补丁提出了一些具体问题和建议，包括是否可以删除某些条件判断，以及是否应在特定配置中添加 CONFIG_PTDUMP_DEBUGFS。Anshuman 对这些建议表示赞同，并确认将进行相应的修改。这些讨论表明，补丁的细节正在逐步完善，参与者积极协作以确保补丁的准确性和有效性。

#### 📝 邮件列表

1. **[02-17 09:52]** [PATCH V2 0/5] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-17 09:52]** [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-17 09:52]** [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-24 13:01]** Re: [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
5. **[02-24 13:04]** Re: [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from
 mpc885_ads_defconfig
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
6. **[02-24 19:18]** Re: [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from
 mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-24 19:19]** Re: [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH 00/14] KVM: arm64: NV userspace ABI

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 15 Feb 2025 17:38:02 +0000

#### 🤖 AI 总结

本邮件线程讨论了与 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的嵌套虚拟化（NV）用户空间 ABI 相关的补丁系列。Marc Zyngier 提出的补丁旨在修正之前版本的 ABI 中存在的细微错误，使其更符合 KVM 的当前操作方式。补丁中移除了对 NV 特定调整的需求，并通过 vcpu 标志完全选择 NV 配置。

在历史讨论中，Marc 提出了多个补丁，包括处理 NV_frac 作为 NV2 的同义词，以及在 VHE（虚拟化扩展）禁用时强制 HCR.EL2.E2H 为 RES0 的补丁。这些补丁的目的是确保在不同的虚拟化环境下，KVM 能够正确处理嵌套虚拟化的特性。

在本周的新讨论中，Aneesh Kumar K.V 针对补丁提出了几个问题和建议，主要集中在对某些寄存器检查的合理性以及代码的优化方面。他指出了补丁中寄存器名称的错误，并讨论了是否需要对某些标志的检查进行调整。Marc 对于这些讨论表示感谢，并确认了之前已有人提出类似的问题。

总体来看，本周的讨论主要围绕补丁的细节和潜在的优化进行，尚未达成最终结论。

#### 📝 邮件列表

1. **[02-15 17:38]** [PATCH 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-15 17:38]** [PATCH 01/14] arm64: cpufeature: Handle NV_frac as a synonym of NV2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-15 17:38]** [PATCH 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-24 13:09]** Re: [PATCH 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when
 ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
5. **[02-24 13:11]** Re: [PATCH 01/14] arm64: cpufeature: Handle NV_frac as a synonym of
 NV2
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
6. **[02-24 08:26]** Re: [PATCH 01/14] arm64: cpufeature: Handle NV_frac as a synonym of NV2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-24 08:32]** Re: [PATCH 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH 0/3] KVM: arm64: Separate the hyp FF-A buffers init from the host

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 26 Feb 2025 21:48:50 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要目的是将超管（hypervisor）FF-A（Firmware Framework for Arm）缓冲区的初始化与主机的调用路径分离。补丁内容包括三个部分：使用静态初始化器替换超管版本锁的定义、在 FF-A 初始化时映射超管的缓冲区、以及向 Trustzone 释放超管接收缓冲区的所有权。

在之前的讨论中，补丁的背景是为了提高系统在受保护模式下的稳定性，确保如果超管无法通过 Trustzone 映射缓冲区，则拒绝任何 FF-A 调用。此外，补丁还将错误映射的定义从 arm_ffa 驱动程序移至 ffa 头文件，以便 hyp 代码可以使用。

本周的新讨论中，参与者 Sudeep Holla 建议将从驱动程序到头文件的代码移动单独作为一个补丁提交，以避免与其他更改的冲突。Sebastian Ene 同意了这一建议，并表示将更新补丁版本。这表明讨论的重点在于代码组织和提交的清晰性，以便于后续的维护和版本管理。

#### 📝 邮件列表

1. **[02-26 21:48]** [PATCH 0/3] KVM: arm64: Separate the hyp FF-A buffers init from the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
2. **[02-26 21:48]** [PATCH 1/3] KVM: arm64: Use the static initializer for the vesion lock
   - 发件人: Sebastian Ene <sebastianene@google.com>
3. **[02-26 21:48]** [PATCH 2/3] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
4. **[02-26 21:48]** [PATCH 3/3] KVM: arm64: Release the ownership of the hyp rx buffer to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
5. **[02-27 09:58]** Re: [PATCH 2/3] KVM: arm64: Map the hypervisor FF-A buffers on ffa
 init
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
6. **[02-27 17:58]** Re: [PATCH 2/3] KVM: arm64: Map the hypervisor FF-A buffers on ffa
 init
   - 发件人: Sebastian Ene <sebastianene@google.com>

---

### Thread 20: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 18 Feb 2025 17:34:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上可写的 MIDR（机器 ID 注册表）和 REVIDR（修订 ID 注册表）的补丁系列。该补丁的目的是允许虚拟机监控器（VMM）在不同机器之间迁移时修改这些寄存器，以便更好地处理错误和兼容性问题。该补丁系列的前提是 errata 管理系列的实现。

在历史讨论中，Sebastian Ott 提到了补丁的变化，包括处理 VPIDR_EL2 的上下文、让来宾观察到 MIDR_EL1 的变化、增加了自测功能等。此补丁系列经过多次版本迭代，旨在解决现有 KVM 的一些限制。

在本周的新讨论中，Oliver Upton 对补丁提出了一些担忧，包括 KVM 允许来宾读取 SMIDR_EL1 的问题，以及当前 KVM 在处理大小核架构时的局限性。他表示将对补丁进行重新工作，以解决这些问题并确保向稳定版本的提交不会破坏现有功能。Sebastian 对 Oliver 的反馈表示感谢，并表示他会继续测试和改进补丁。整体来看，讨论集中在补丁的兼容性和稳定性上，参与者积极寻求解决方案。

#### 📝 邮件列表

1. **[02-18 17:34]** [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-24 14:23]** Re: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-26 17:47]** Re: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[02-26 10:56]** Re: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9

**📧 邮件数**: 4 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 24 Feb 2025 14:11:28 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁，主题为“[PATCH V2 7/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”。该补丁旨在启用与 PMUv3.9 相关的 EL2 要求，确保在特定条件下正确配置相关寄存器。

在历史讨论中，参与者们关注补丁是否遗漏了必要的寄存器配置，特别是 MDCR_EL3.EnPM2 位的设置，这一位在引导包装程序中默认重置为 0，可能导致 EL{2,1,0} 访问某些寄存器时出现问题。同时，讨论还提到该补丁需要添加稳定性和修复标签，以便进行回溯。

本周的新讨论中，Mark Rutland 指出需要进一步检查补丁是否涵盖了所有 FEAT_PMUv3p9 的要求，并建议可能需要对补丁进行修正或重新提交。Anshuman Khandual 提出更新文档以反映 MDCR_EL3.EnPM2 的设置，并讨论了是否需要检查其他特性。Rob Herring 和 Catalin Marinas 也参与了讨论，确认补丁尚未应用，但建议在重新提交时添加稳定性和修复标签，以便于追踪。

总体而言，本周的讨论集中在补丁的完整性、必要的寄存器配置以及如何处理补丁的提交上。

#### 📝 邮件列表

1. **[02-24 14:11]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[02-25 11:47]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-26 11:14]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Rob Herring <robh@kernel.org>
4. **[02-26 17:44]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 22: [PATCH v2 00/14] KVM: arm64: NV userspace ABI

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 20 Feb 2025 13:48:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 NV（Nested Virtualization）用户空间 ABI（应用二进制接口）的补丁系列。

**原始补丁内容：**
Marc Zyngier 提出的补丁 v2 00/14 旨在修正之前版本中存在的细微错误，使其更符合 KVM 的当前操作方式。补丁中取消了对 NV 特定调整的需求，并通过 vcpu 标志完全选择 NV 配置，保留了 KVM_ARM_VCPU_EL2 标志以启用 VHE（Virtualization Host Extensions），并新增了 KVM_ARM_VCPU_EL2_E2H0 标志，以限制 NV 行为仅支持 nVHE（non-VHE）来宾。

**之前讨论要点：**
在历史讨论中，Marc 提到 NV 的复杂性，并提出了两种相互排斥的配置：VHE-only 和 mVHE-only。为此，补丁引入了一个新的 vcpu 特性标志，以进一步限制 ID 寄存器的功能。

**本周的新讨论与进展：**
本周，Aneesh Kumar K.V 对补丁进行了简要评论，指出了一个术语的修正（将 mVHE-only 更正为 nVHE-only）。Oliver Upton 则报告了对补丁的修正，包括修复了导致 bisection 失败的拼写错误，并表示已将补丁应用到下一个版本中，感谢参与者的贡献。整体来看，补丁系列得到了积极的反馈，并在逐步完善中。

#### 📝 邮件列表

1. **[02-20 13:48]** [PATCH v2 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-20 13:49]** [PATCH v2 10/14] KVM: arm64: Allow userspace to limit NV support to nVHE
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-24 15:14]** Re: [PATCH v2 10/14] KVM: arm64: Allow userspace to limit NV
 support to nVHE
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
4. **[02-24 11:52]** Re: (subset) [PATCH v2 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 23: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 10:12:19 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是关于移除 arm64 架构中的 PXD_TABLE_BIT 的补丁（PATCH V2 0/8）。该补丁的主要内容是删除 PXX_TABLE_BIT 定义，转而依赖于 PXX_TYPE_MASK、PXX_TYPE_SECT 和 PXX_TYPE_TABLE。这种抽象方式对于即将支持的 D128 页表非常重要，因为 D128 页表没有单一的页表位来区分表和块，而是使用跳过级别（SKL）字段。

在历史讨论中，Anshuman Khandual 提出了这一补丁，并强调了其在未来支持 D128 页表时的必要性。

在本周的新讨论中，Anshuman Khandual 询问了补丁系列的进展。Ryan Roberts 对补丁的逻辑正确性表示认可，但建议将所有移除 PXX_TABLE_BIT 的修改合并为一个补丁，并将 pud_bad() 的修复（当前为第六个补丁）单独处理。他认为这样可以简化审查过程，并提供更清晰的提交日志。Ryan 还提到，虽然他是原始补丁的作者，但他认为不应在此提供审核意见。

总的来说，讨论围绕补丁的结构和审查过程展开，参与者对补丁的目的表示支持，但对补丁的组织形式提出了改进建议。

#### 📝 邮件列表

1. **[02-21 10:12]** [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-28 09:12]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-28 15:32]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>

---

### Thread 24: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 1 Mar 2025 07:58:50 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 启动的补丁系列，主题为“[PATCH V2 0/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”。该补丁旨在启用 EL2 级别对 PMUv3p9 特性的要求。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁系列的前六个补丁已经被应用，并得到了参与者的认可。Will Deacon 在邮件中确认补丁 1-6 与相关的 XML 文件对比是正确的，并表示支持。

在本周的新讨论中，Will Deacon 对补丁的状态进行了更新，确认补丁 1-6 已经被应用，同时提到最后一个补丁将被 Catalin Marinas 删除或替换。Catalin 随后确认他已经删除了最后一个补丁，并表示将排队处理新的补丁。

总体来看，本周的讨论主要集中在对补丁状态的确认和后续处理上，表明开发团队在推进 ARM64 启动相关功能的过程中保持了良好的沟通与协作。

#### 📝 邮件列表

1. **[03-01 07:58]** Re: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Will Deacon <will@kernel.org>
2. **[03-01 11:11]** Re: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 25: [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 02 Mar 2025 17:12:54 +0900

#### 🤖 AI 总结

本周讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的性能监控单元（PMU）相关的一个补丁，旨在修复 vPMC（虚拟性能监控计数器）寄存器的 SET_ONE_REG 操作。补丁的主要内容是，当设置 vPMC 寄存器（如 PMCCNTR_EL0 和 PMEVCNTR<n>_EL0）时，重置当前的性能事件计数器，以确保寄存器的当前值正确反映。

在之前的讨论中，提到过一个相关的补丁（commit 9228b26194d1），该补丁修复了 GET_ONE_REG 操作，使其能够返回 vPMC 寄存器的当前值。然而，SET_ONE_REG 操作在更新寄存器值时未能重置当前性能事件计数器，导致保存的寄存器值与实际计数不符。

本周的邮件中，Akihiko Odaki 提出了这个补丁，并详细描述了如何通过调用 `kvm_pmu_set_counter_value()` 函数来修复这一问题，以确保在用户空间写入寄存器时，当前性能事件计数器的值也会被重置。这一补丁的实施将提高 vPMC 寄存器的准确性和一致性。

#### 📝 邮件列表

1. **[03-02 17:12]** [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>

---

### Thread 26: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 28 Feb 2025 12:13:55 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在统计 pKVM（Paravirtualized KVM）在二级页表中的使用情况。该补丁通过在内存统计中增加 pKVM 使用的页面计数，类似于 VHE（Virtualization Host Extensions）模式的做法。

在本周的讨论中，Vincent Donnefort 提出了这个补丁，具体内容包括在 `hyp_mc_alloc_fn` 和 `hyp_mc_free_fn` 函数中增加对页表页面的计数。补丁的代码修改部分显示了如何在分配和释放内存时更新页表页面的统计信息，以便更好地反映 pKVM 的内存使用情况。

此次讨论没有提及之前的相关讨论或补丁，因此本周的进展主要集中在补丁的具体实现和其目的上。整体来看，此补丁的提出旨在提升 KVM 在处理二级页表时的内存管理能力，为后续的性能优化和资源监控提供支持。

#### 📝 邮件列表

1. **[02-28 12:13]** [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 27: [PATCH v4] arm64: Add basic MTE test

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 27 Feb 2025 15:22:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构中添加基本的内存标签扩展（MTE）测试的补丁（PATCH v4）。该补丁的主要内容是测试标签存储访问和不同 MTE 模式下的标签不匹配情况。补丁中涉及了多个文件的修改，包括添加了新的测试文件 `mte.c`，并在 `Makefile` 中注册了相关测试。

在历史讨论中并没有提供具体的背景信息，因此我们无法了解之前的讨论要点。

在本周的新讨论中，Vladimir Murzin 提交了这个补丁，并详细描述了补丁的实现，包括如何处理标签检查故障、内存读写操作以及如何设置和清除标签。补丁还包括了对不同 MTE 模式的测试，如同步、异步和不对称测试，确保在不同情况下的标签检查能够正常工作。

总的来说，本周的讨论集中在补丁的实现细节和测试方法上，显示出对 MTE 功能的深入探索和验证。

#### 📝 邮件列表

1. **[02-27 15:22]** [PATCH v4] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>

---

### Thread 28: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 27 Feb 2025 09:21:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的补丁 [PATCH V3]，旨在启用 FEAT_PMUv3p9 的 EL2 要求。该补丁涉及对 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 寄存器的访问控制，要求通过 FEAT_FGT2 的细粒度陷阱控制寄存器 HDFGRTR2_EL2 和 HDFGWTR2_EL2 进行适当配置，否则将导致陷入 EL2。

在之前的讨论中，补丁经历了多个版本的修改，主要集中在确保 EL2 的细粒度陷阱控制寄存器的初始化，以便正确访问 PMU 寄存器。此外，补丁还更新了文档，明确了 SCR_EL3.FGTEn2 的要求。

本周的新讨论中，补丁的最终版本被提交，增加了 MDCR_EL3.EnPM2 的初始化要求，并添加了相关的修复和稳定性标签。补丁经过了 Rob Herring 的测试和审核，确认其功能和稳定性。整体来看，该补丁为 ARM64 架构的性能监控功能提供了必要的支持和配置要求。

#### 📝 邮件列表

1. **[02-27 09:21]** [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 17:45:26 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 单元测试库的补丁提案，主题为将 `__ASSEMBLY__` 替换为 `__ASSEMBLER__`。该补丁的目的是将所有非 x86 的条件编译指令从 `__ASSEMBLY__` 修改为 `__ASSEMBLER__`，并移除手动定义的 `__ASSEMBLY__`。`__ASSEMBLY__` 是从 Linux 内核继承而来，需要手动定义，而 `__ASSEMBLER__` 则由编译器自动定义，避免了手动定义带来的问题。

在历史讨论中，Sean Christopherson 提出了这一补丁，并指出 x86 架构不在考虑范围内。补丁的目的是为了提高代码的可维护性和可靠性。

在本周的新讨论中，Andrew Jones 对该补丁进行了审查，并指出在 `lib/libfdt/fdt.h` 文件中还有一个拼写错误的 `__ASSEMBLY__`，他建议将其替换。最终，Andrew 表达了对补丁的支持，并表示已审核通过。这表明该补丁在社区中得到了积极的反馈，向前推进了一步。

#### 📝 邮件列表

1. **[02-21 17:45]** [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[02-25 14:37]** Re: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of
 __ASSEMBLY__
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.14, take #3

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 17:44:06 +0000

#### 🤖 AI 总结

在本次邮件讨论中，Marc Zyngier 提出了针对 KVM/arm64 的修复补丁，旨在解决 Linux 6.14 版本中的 MMU 相关错误。具体问题包括在 hVHE EL2 的 stage-1 中，ASID 从错误的寄存器中获取，以及 VHE 运行时使用过时的 VMID 值。这些问题被认为是严重的缺陷，影响了系统的稳定性。

在之前的讨论中，Marc 强调了这些错误的严重性，并请求 Paolo 进行合并。邮件中提到的补丁是基于 2025 年 2 月 16 日的 Linux 6.14-rc3 版本的更新。

在本周的新讨论中，Paolo Bonzini 对 Marc 的请求进行了回应，表示已经成功合并了这些修复补丁，并对 Marc 的工作表示感谢。这表明补丁已经获得了认可并被纳入了主线代码中，标志着问题的解决和进展。

#### 📝 邮件列表

1. **[02-20 17:44]** [GIT PULL] KVM/arm64 fixes for 6.14, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-24 19:20]** Re: [GIT PULL] KVM/arm64 fixes for 6.14, take #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 13:57:38 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 KVM 单元测试中为 arm64 架构添加基本 MTE（内存跟踪扩展）测试的补丁（PATCH v3）。该补丁旨在增强对 MTE 功能的测试，确保其在不同情况下的正确性。

在之前的讨论中，参与者们关注了可能导致 PTE（页面表项）查找失败的多种问题，包括 `follow_pte()` 函数的错误、页面分配器的缺陷以及 arm64 内存映射代码中的问题。尽管这些问题可能导致测试失败，但大多数测试并不检查页面分配器返回 NULL 的情况，因此并不常见。参与者们一致认为这个测试非常有用，并且已经在讨论列表中存在了一段时间，因此不认为这是一个阻碍因素。

在本周的新讨论中，Alexandru Elisei 表达了对补丁的认可，并提到将其合并的意愿。同时，Andrew Jones 询问是否会有 v4 版本的补丁。Vladimir Murzin 回复表示会根据 Alex 的反馈进行相应的修改。整体来看，补丁得到了积极的反馈，且参与者们对其后续进展持乐观态度。

#### 📝 邮件列表

1. **[02-27 13:57]** Re: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[02-27 15:29]** Re: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[02-27 14:33]** Re: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v1 0/7] arm64: support EL2

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 14:13:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 单元测试的补丁系列，主要目的是为 EL2（异常级别 2）提供支持。这一系列补丁包括七个部分，涉及到在 EL2 下的启动、定时器、微基准测试、自检和性能监控单元（PMU）等方面的修改。

在历史讨论中，参与者 Joey Gouly 提出了补丁的初步版本，并指出当前 EL2 的支持尚不完善，部分测试未通过，尤其是在嵌套虚拟化和调试测试方面。补丁的目标是为未来的嵌套虚拟化测试奠定基础，并确保这些测试在裸机环境下也能正常运行。

本周的新讨论中，参与者 Alexandru Elisei 对补丁进行了逐一审查，提出了一些细节性的问题和建议。他确认了多个补丁的正确性，并指出了某些补丁中作者信息的遗漏。此外，他对 PMU 计数逻辑的实现提出了疑问，特别是关于在 EL2 下事件计数的有效性和不同宏的使用方式。

总体来看，本周的讨论主要集中在对补丁的审查和细节上的优化，参与者之间的互动为补丁的完善提供了有价值的反馈。

#### 📝 邮件列表

1. **[02-20 14:13]** [kvm-unit-tests PATCH v1 0/7] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[02-20 14:13]** [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[02-20 14:13]** [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[02-20 14:13]** [kvm-unit-tests PATCH v1 3/7] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[02-20 14:13]** [kvm-unit-tests PATCH v1 5/7] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[02-20 14:13]** [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[02-27 16:53]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[02-27 16:55]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[02-27 16:58]** Re: [kvm-unit-tests PATCH v1 3/7] arm64: micro-bench: fix timer IRQ
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[02-27 16:58]** Re: [kvm-unit-tests PATCH v1 5/7] arm64: selftest: update test for
 running at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[02-27 17:01]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: writable ID_AA64MMFR0_EL1.TGRAN*_2 ?

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 28 Feb 2025 16:19:06 +0100 (CET)

#### 🤖 AI 总结

本邮件讨论的主题是关于可写的 ID_AA64MMFR0_EL1.TGRAN*_2 寄存器。发件人 Sebastian Ott 提出希望在两个 Graviton 主机之间迁移时，能够处理这两个主机在 TGRAN*_2 寄存器上的差异。目前这两个主机支持相同的 S2 大小，但在表达方式上存在不同（一个为 2 表示支持，另一个为 0 表示“查看 TGRAN*”）。

Sebastian 提出了两个可能的解决方案：一是将这些寄存器的访客视图设置为 NI（不适用）以适应“普通”或非嵌套的访客；二是允许在这两个值之间进行转换，并可能允许写入 NI 值以确保兼容性。

目前尚无其他参与者的回复或进一步讨论，因此这一提议仍在初步阶段。整体来看，本周的讨论集中在如何解决 Graviton 主机间寄存器差异的问题上，以便实现更顺畅的虚拟机迁移。

#### 📝 邮件列表

1. **[02-28 16:19]** writable ID_AA64MMFR0_EL1.TGRAN*_2 ?
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

