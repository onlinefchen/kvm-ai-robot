# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 07:52:50

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 78
- **总 Thread 数**: 10
- **大型 Thread** (>20封): 1 个

### 分类分布

- **PATCH**: 6 threads (20 邮件)
- **RFC**: 2 threads (15 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 1 threads (41 邮件)

---

## 📌 PATCH

共 6 个 thread

---

### Thread 1: [PATCH v5 0/4] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 24 Jan 2025 15:17:28 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 平台上虚拟机实时迁移的错误管理的补丁（PATCH v5 0/4）。该补丁旨在解决在迁移过程中，因不同平台的 CPU MIDR/REVIDR 值导致的错误处理问题。

在历史讨论中，补丁的背景提到，ARM64 平台上的许多错误处理方案依赖于 CPU 的 MIDR/REVIDR 值，而这些方案需要在客户机内核中实现。这在迁移到不同 MIDR/REVIDR 值的硬件时会造成问题。Shameer Kolothum 提到这是基于与 Marc 和 Oliver 在 KVM 论坛的讨论，Marc 提出了一个解决方案的构想。

本周的新讨论中，Shameer 提交了补丁 v5，主要更新包括：
1. 增加了一个超调用（hypercall），用于从用户空间的虚拟机监控器（VMM）获取目标 CPU 实现的版本和数量。
2. 增加了对 KVM 超调用服务可用性的检查。
3. 移除了部分 R-by 标签，因为补丁 2 和 4 有所修改。

此外，补丁还包括了对现有函数的修改，以支持客户机内核利用 VMM 提供的目标 CPU 实现，并在迁移时启用相关的错误处理。Shameer 邀请参与者对补丁进行审查并提供反馈。整体来看，讨论集中在如何改进 KVM 的错误管理机制，以支持更灵活的虚拟机迁移。

#### 📝 邮件列表

1. **[01-24 15:17]** [PATCH v5 0/4] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[01-24 15:17]** [PATCH v5 1/4] arm64: Modify _midr_range() functions to read MIDR/REVIDR internally
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
3. **[01-24 15:17]** [PATCH v5 2/4] KVM: arm64: Introduce hypercall support for retrieving target implementations
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
4. **[01-24 15:17]** [PATCH v5 3/4] KVM: arm64: Report all the KVM/arm64-specific hypercalls
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
5. **[01-24 15:17]** [PATCH v5 4/4] arm64: paravirt: Enable errata based on implementation CPUs
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>

---

### Thread 2: [PATCH v2 09/12] KVM: arm64: nv: Propagate
 CNTHCTL_EL2.EL1NV{P,V}CT bits

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 6 Jan 2025 10:33:39 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 ARM64 架构下对 CNTHCTL_EL2.EL1NV{P,V}CT 位的传播的补丁（PATCH v2 09/12）。该补丁旨在解决 KVM ARM 中关于虚拟化的约束问题，尤其是与非虚拟化（NV）相关的内容。

在历史讨论中，Wei-Lin Chang 提出了对 NV 和 E2H 约束的疑问，Marc Zyngier 指出这些约束在 kvm-arm64/nv-e2h-select 分支中得到了执行，并强调了理解这一系列补丁的重要性，以便更好地连接相关代码。

本周的新讨论中，Wei-Lin Chang 表示他对之前的讨论有了更深的理解，并意识到需要研究更多复杂的代码。同时，Volodymyr Babchuk 提出了在 Amazon Graviton 4 平台上使用该系列补丁启动 Xen 时遇到的问题，指出在处理 EL2 定时器状态时存在覆盖问题，导致 Xen 写入的定时器值被错误地覆盖。Babchuk 询问对此问题的正确修复方案，并提到在 Dom0 中也观察到与定时器相关的问题，但尚未确定具体原因。

总体而言，讨论围绕补丁的实施细节和在特定平台上的兼容性问题展开，参与者们积极探讨解决方案。

#### 📝 邮件列表

1. **[01-06 10:33]** Re: [PATCH v2 09/12] KVM: arm64: nv: Propagate
 CNTHCTL_EL2.EL1NV{P,V}CT bits
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[01-17 15:19]** Re: [PATCH v2 09/12] KVM: arm64: nv: Propagate CNTHCTL_EL2.EL1NV{P,V}CT bits
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-21 14:04]** Re: [PATCH v2 09/12] KVM: arm64: nv: Propagate
 CNTHCTL_EL2.EL1NV{P,V}CT bits
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[01-26 15:25]** Re: [PATCH v2 02/12] KVM: arm64: nv: Sync nested timer state with
 FEAT_NV2
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>

---

### Thread 3: [PATCH RFC v3 09/27] KVM: arm64: Factor SVE guest exit handling
 out into a function

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 17 Jan 2025 11:34:09 +0000

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH RFC v3 09/27] KVM: arm64: 将 SVE 客户端退出处理提取为一个函数”。该补丁旨在改进 KVM 在 arm64 架构下对 SVE（Scalable Vector Extension）状态的处理。

**历史讨论**中，Mark Rutland 提到在调查 SVE 相关问题时发现了一个潜在的错误，可能与之前的提交（8c8010d69c132273）有关，该提交涉及 nVHE（Non-Virtual Hypervisor Extension）下 SVE 状态的保存和恢复。他对当前代码中 IRQ（中断请求）处理的方式表示怀疑，认为在某些情况下可能会引发问题。

**本周新讨论**中，Marc Zyngier 和 Mark Rutland 继续探讨如何优化 SVE 状态的保存和恢复。Marc 提出是否应该提前保存和恢复 ZCR_ELx 寄存器，Mark 表示赞同，并表示会进一步确认并进行相应的修改。这表明在处理 SVE 状态时，开发者们正在积极寻求解决方案，以确保系统的稳定性和性能。

总体来看，本周的讨论集中在如何有效地解决历史讨论中提到的问题，并推动补丁的进一步完善。

#### 📝 邮件列表

1. **[01-17 11:34]** Re: [PATCH RFC v3 09/27] KVM: arm64: Factor SVE guest exit handling
 out into a function
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[01-22 11:51]** Re: [PATCH RFC v3 09/27] KVM: arm64: Factor SVE guest exit handling out into a function
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-22 11:56]** Re: [PATCH RFC v3 09/27] KVM: arm64: Factor SVE guest exit handling
 out into a function
   - 发件人: Mark Rutland <mark.rutland@arm.com>

---

### Thread 4: [PATCH] KVM: arm64: Flush hyp bss section after initialization of
 variables in bss

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 20 Jan 2025 15:15:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在解决在初始化 BSS（未初始化数据段）后未能正确刷新数据的问题。

**原始补丁内容**：
补丁的主要目的是在初始化 BSS 段中的变量后，刷新整个 BSS 段，以确保 EL2 能够正确读取 CPU 特性寄存器的值。当前的实现中，由于未能刷新这些变量，导致 EL2 看到的值为 0，从而引发了一系列问题，包括内核崩溃。

**之前讨论要点**：
在之前的讨论中，参与者指出，单独刷新每个变量效率低下，因此提出了整体刷新 BSS 的方案。然而，Marc Zyngier 对此提出质疑，认为在 hypervisor 初始化后再进行刷新可能并不能解决问题，并且可能会导致访问违规。

**本周新讨论及进展**：
在本周的讨论中，Lokesh Vutla 对 Marc 的反馈做出了回应，承认之前的实现存在问题，并表示将会在 `kvm_hyp_init_symbols()` 函数中添加刷新操作，以确保在 EL2 初始化之前正确处理数据。Lokesh 还提到，之前的测试表明逐个刷新变量的方式能够正常工作，但在优化过程中可能出现了错误的刷新时机。计划在下一个版本中修正这些问题并重新提交补丁。

#### 📝 邮件列表

1. **[01-20 15:15]** [PATCH] KVM: arm64: Flush hyp bss section after initialization of
 variables in bss
   - 发件人: Lokesh Vutla <lokeshvutla@google.com>
2. **[01-20 16:13]** Re: [PATCH] KVM: arm64: Flush hyp bss section after initialization of variables in bss
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-21 09:54]** Re: [PATCH] KVM: arm64: Flush hyp bss section after initialization of
 variables in bss
   - 发件人: Lokesh Vutla <lokeshvutla@google.com>

---

### Thread 5: [PATCH kvmtool v1 0/2] Error handling fixes

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 20 Jan 2025 16:17:58 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 kvmtool 的错误处理修复，包含两个补丁。第一个补丁旨在改进 VCPU 线程的错误代码传播，确保在 VCPU 0 出现错误时能够正确返回非零退出代码，避免错误被覆盖为成功。第二个补丁则是将关于地址转换失败的警告信息调整为调试信息，以减少冗余和误导。

在历史讨论中，未提供具体背景信息，但本周的讨论集中在这两个补丁的具体实现和必要性上。Alexandru Elisei 提到，当前的实现存在几个问题，例如 VCPU 0 的错误代码未被捕获，导致 kvmtool 在出错时仍返回成功状态。此外，错误信息的打印方式也可能导致用户混淆，因此将其改为调试信息以便于开发者在需要时查看。

本周的进展包括补丁的具体代码实现和逻辑说明，强调了这些修复对提高 kvmtool 错误处理能力的重要性。整体来看，这些改进旨在提升 kvmtool 的稳定性和可用性。

#### 📝 邮件列表

1. **[01-20 16:17]** [PATCH kvmtool v1 0/2] Error handling fixes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[01-20 16:17]** [PATCH kvmtool v1 1/2] Propagate the error code from any VCPU thread
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[01-20 16:18]** [PATCH kvmtool v1 2/2] Do not a print a warning on failing host<->guest address translation
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 6: [PATCH v2] KVM: arm64: Flush hyp bss section after initialization of
 variables in bss

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 21 Jan 2025 04:40:16 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及在初始化 bss 段变量后刷新 hyp bss 段的内容。

1. **原始 patch/问题内容**：
   该补丁（[PATCH v2]）旨在确保在 KVM 的 nVHE（非虚拟化高效）hypervisor 初始化过程中，能够正确地刷新存储在 bss 段中的 CPU 特性寄存器的值。这些值在 kvm_hyp_init_symbols() 函数中被更新，为了在 MMU 关闭的情况下确保 EL2 可见性，需要在更新后刷新数据缓存。补丁建议在初始化完成后一次性刷新整个 bss 段，而不是逐个刷新变量。

2. **之前讨论要点**：
   该补丁是基于之前的讨论和补丁（6c30bfb18d0b）进行的改进，主要是为了提高效率，避免逐个刷新变量的低效做法。补丁的提交者 Lokesh Vutla 在 v1 版本中收到了反馈，并根据审查意见更新了提交信息和代码。

3. **本周的新讨论、进展或结论**：
   在本周的讨论中，Marc Zyngier 对补丁表示认可，并确认已将其应用于修复列表中。这表明该补丁已获得通过，进一步推动了 KVM 在 arm64 架构下的改进进程。

#### 📝 邮件列表

1. **[01-21 04:40]** [PATCH v2] KVM: arm64: Flush hyp bss section after initialization of
 variables in bss
   - 发件人: Lokesh Vutla <lokeshvutla@google.com>
2. **[01-21 08:40]** Re: [PATCH v2] KVM: arm64: Flush hyp bss section after initialization of variables in bss
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM

**📧 邮件数**: 14 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 8 Jan 2025 12:09:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的 Arm SMMUv3 驱动程序的 RFC PATCH v2，主要针对 pKVM 的实现。

1. **原始 patch/问题的内容**：该补丁旨在为 pKVM 提供 Arm SMMUv3 驱动，重点在于如何处理主机和客户机之间的地址转换，以及如何在不同的虚拟化场景中实现 IOMMU 的支持。

2. **之前的讨论要点**：历史讨论中，参与者探讨了主机与客户机在 IOMMU 管理上的不同，特别是嵌套翻译的必要性。Jason Gunthorpe 强调了主机和客户机在处理 DMA 和 IOMMU 方面的差异，Kevin Tian 则提到需要考虑如何在 pKVM 中实现更好的初始化和代码复用。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Mostafa Saleh 提出了简化补丁系列的计划，建议去掉部分复杂的 para-virtualization 代码，专注于建立 DMA 隔离的基础。Jason Gunthorpe 和 Kevin Tian 也对如何处理地址映射和性能影响进行了深入讨论，强调了在设计 pKVM 时需要考虑的复杂性和未来的可维护性。总体来看，参与者们达成了共识，即在设计中应优先考虑简化和可扩展性。

#### 📝 邮件列表

1. **[01-08 12:09]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[01-16 06:39]** RE: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Tian, Kevin <kevin.tian@intel.com>
3. **[01-16 08:51]** RE: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Tian, Kevin <kevin.tian@intel.com>
4. **[01-16 15:14]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
5. **[01-16 15:19]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
6. **[01-17 06:57]** RE: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Tian, Kevin <kevin.tian@intel.com>
7. **[01-22 11:04]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[01-22 11:28]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[01-22 11:46]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[01-22 12:20]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
11. **[01-22 17:17]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[01-22 15:16]** Re: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
13. **[01-23 08:13]** RE: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Tian, Kevin <kevin.tian@intel.com>
14. **[01-23 08:25]** RE: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Tian, Kevin <kevin.tian@intel.com>

---

### Thread 2: [RFC PATCH v2 27/58] KVM: arm64: smmu-v3: Setup command queue

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 23 Jan 2025 13:01:55 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 SMMU v3（System Memory Management Unit v3）命令队列设置的 RFC（请求反馈）补丁（patch）。该补丁旨在改进 SMMU v3 的命令处理机制，以提升虚拟化性能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了应对当前内核驱动中存在的一些问题，尤其是与命令序列生成相关的错误处理（errata）机制。

本周的讨论中，参与者 Robin Murphy 对 Mostafa Saleh 提出的补丁进行了回应，提醒其在实现过程中需要重新处理一些错误修正，以避免生成特定的有问题的命令序列。他指出，这些问题在当前的内核驱动中是隐含存在的，强调了实现的复杂性和潜在的挑战。

总体来看，本周的讨论主要集中在补丁实施的细节和潜在问题上，参与者对补丁的复杂性表示关注，特别是在处理错误修正方面。

#### 📝 邮件列表

1. **[01-23 13:01]** Re: [RFC PATCH v2 27/58] KVM: arm64: smmu-v3: Setup command queue
   - 发件人: Robin Murphy <robin.murphy@arm.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 updates for 6.14

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 17 Jan 2025 11:52:08 +0000

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.14 版本中的更新。历史讨论中，Marc Zyngier 提出了初步的 KVM/arm64 变更集，主要集中在调试和保护模式的清理工作上。此外，新增了对非保护模式来宾的支持、EL2 定时器支持以及改进的 CoreSight 支持。该更新还包括了一些常规的代码清理和错误修复，并提到需要解决的两个分支冲突。

在本周的新讨论中，Paolo Bonzini 对 Marc 的更新表示感谢，并确认已将这些更改合并。这表明 KVM/arm64 的更新工作得到了认可，并且进展顺利。整体来看，讨论主要围绕 KVM/arm64 的功能增强和代码维护，显示出社区对改进和稳定性的持续关注。

#### 📝 邮件列表

1. **[01-17 11:52]** [GIT PULL] KVM/arm64 updates for 6.14
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-20 13:02]** Re: [GIT PULL] KVM/arm64 updates for 6.14
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 00/18] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 41 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 20 Jan 2025 16:42:58 +0000

#### 🤖 AI 总结

本邮件线程讨论了对 KVM 单元测试框架的更新，主要是添加对 kvmtool 的支持。以下是讨论的主要内容：

1. **原始 patch/问题的内容**：
   - Alexandru Elisei 提交了一系列补丁（PATCH v2 00/18），目的是将 kvmtool 集成到 `run_tests.sh` 脚本中，以便用户可以更方便地运行测试。kvmtool 是一个轻量级的虚拟机管理程序，相较于 QEMU 更易于修改和快速运行测试。

2. **之前的讨论要点**：
   - 之前的讨论集中在如何将大型补丁拆分为多个小补丁，以便于审查。补丁中增加了多个新参数和功能，例如 `kvmtool_params` 和 `disabled_if`，后者用于在特定条件下跳过不支持的测试。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论主要围绕补丁的审查和修改建议。Andrew Jones 对多个补丁进行了审核，提出了关于参数命名和代码结构的建议，如使用更通用的参数名称以减少重复。此外，讨论还涉及到如何处理 kvmtool 和 QEMU 的不同命令行参数，以及如何在测试中使用 `disabled_if` 参数来跳过不适用的测试。最终，补丁被确认可以启用 kvmtool 支持，并移除了与 ERRATA_FORCE 相关的配置，以简化测试运行。

总的来说，这一系列补丁的目标是增强 KVM 单元测试框架的灵活性和可用性，使其能够在不同的虚拟机管理程序下运行测试。

#### 📝 邮件列表

1. **[01-20 16:42]** [kvm-unit-tests PATCH v2 00/18] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[01-20 16:42]** [kvm-unit-tests PATCH v2 01/18] run_tests: Document --probe-maxsmp argument
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[01-20 16:43]** [kvm-unit-tests PATCH v2 02/18] Document environment variables
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[01-20 16:43]** [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[01-20 16:43]** [kvm-unit-tests PATCH v2 04/18] run_tests: Introduce unittest parameter 'qemu_params'
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[01-20 16:43]** [kvm-unit-tests PATCH v2 05/18] scripts: Rename run_qemu_status -> run_test_status
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[01-20 16:43]** [kvm-unit-tests PATCH v2 06/18] scripts: Merge the qemu parameter -smp into $qemu_opts
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[01-20 16:43]** [kvm-unit-tests PATCH v2 07/18] scripts: Introduce kvmtool_opts
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[01-20 16:43]** [kvm-unit-tests PATCH v2 08/18] scripts/runtime: Detect kvmtool failure in premature_failure()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[01-20 16:43]** [kvm-unit-tests PATCH v2 09/18] scripts/runtime: Skip test when kvmtool and $accel is not KVM
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[01-20 16:43]** [kvm-unit-tests PATCH v2 10/18] scripts/arch-run: Add support for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[01-20 16:43]** [kvm-unit-tests PATCH v2 11/18] arm/run: Add support for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[01-20 16:43]** [kvm-unit-tests PATCH v2 12/18] scripts/runtime: Add default arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
14. **[01-20 16:43]** [kvm-unit-tests PATCH v2 13/18] run_tests: Do not probe for maximum number of VCPUs when using kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
15. **[01-20 16:43]** [kvm-unit-tests PATCH v2 14/18] run_tests: Add KVMTOOL environment variable for kvmtool binary path
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
16. **[01-20 16:43]** [kvm-unit-tests PATCH v2 15/18] Add kvmtool_params to test specification
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
17. **[01-20 16:43]** [kvm-unit-tests PATCH v2 16/18] scripts/mkstandalone: Export $TARGET
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
18. **[01-20 16:43]** [kvm-unit-tests PATCH v2 17/18] unittest: Add disabled_if parameter and use it for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
19. **[01-20 16:43]** [kvm-unit-tests PATCH v2 18/18] run_tests: Enable kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
20. **[01-21 15:41]** Re: [kvm-unit-tests PATCH v2 01/18] run_tests: Document
 --probe-maxsmp argument
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
21. **[01-21 15:41]** Re: [kvm-unit-tests PATCH v2 02/18] Document environment variables
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
22. **[01-21 15:48]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
23. **[01-21 16:46]** Re: [kvm-unit-tests PATCH v2 04/18] run_tests: Introduce unittest
 parameter 'qemu_params'
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
24. **[01-21 15:54]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
25. **[01-21 16:55]** Re: [kvm-unit-tests PATCH v2 05/18] scripts: Rename run_qemu_status
 -> run_test_status
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
26. **[01-21 17:12]** Re: [kvm-unit-tests PATCH v2 06/18] scripts: Merge the qemu
 parameter -smp into $qemu_opts
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
27. **[01-21 17:17]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
28. **[01-21 16:20]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
29. **[01-21 17:24]** Re: [kvm-unit-tests PATCH v2 07/18] scripts: Introduce kvmtool_opts
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
30. **[01-21 17:29]** Re: [kvm-unit-tests PATCH v2 08/18] scripts/runtime: Detect kvmtool
 failure in premature_failure()
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
31. **[01-21 17:30]** Re: [kvm-unit-tests PATCH v2 09/18] scripts/runtime: Skip test when
 kvmtool and $accel is not KVM
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
32. **[01-21 17:46]** Re: [kvm-unit-tests PATCH v2 10/18] scripts/arch-run: Add support
 for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
33. **[01-21 17:50]** Re: [kvm-unit-tests PATCH v2 11/18] arm/run: Add support for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
34. **[01-23 15:07]** Re: [kvm-unit-tests PATCH v2 12/18] scripts/runtime: Add default
 arguments for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
35. **[01-23 14:20]** Re: [kvm-unit-tests PATCH v2 12/18] scripts/runtime: Add default
 arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
36. **[01-23 16:36]** Re: [kvm-unit-tests PATCH v2 13/18] run_tests: Do not probe for
 maximum number of VCPUs when using kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
37. **[01-23 16:43]** Re: [kvm-unit-tests PATCH v2 14/18] run_tests: Add KVMTOOL
 environment variable for kvmtool binary path
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
38. **[01-23 16:53]** Re: [kvm-unit-tests PATCH v2 15/18] Add kvmtool_params to test
 specification
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
39. **[01-23 16:53]** Re: [kvm-unit-tests PATCH v2 16/18] scripts/mkstandalone: Export
 $TARGET
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
40. **[01-23 17:08]** Re: [kvm-unit-tests PATCH v2 17/18] unittest: Add disabled_if
 parameter and use it for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
41. **[01-23 17:12]** Re: [kvm-unit-tests PATCH v2 18/18] run_tests: Enable kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

