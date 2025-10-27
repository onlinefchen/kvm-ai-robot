# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 08:50:15

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 平台上进行虚拟机实时迁移时的错误管理。Shameer Kolothum 提出了一个包含四个补丁的系列更新（PATCH v5 0/4），旨在改进虚拟机迁移过程中的错误处理。

历史讨论中，补丁的背景是 ARM64 平台上的许多错误解决方案依赖于 CPU 的 MIDR/REVIDR 值，这使得在不同 MIDR/REVIDR 值的平台之间迁移虚拟机时，存在兼容性问题。之前的版本（v1 到 v4）中，Shameer 针对反馈进行了多次修改，增加了超调用（hypercall）以获取目标 CPU 的实现信息，并调整了相关函数以支持这些新特性。

在本周的新讨论中，Shameer 更新了补丁并回应了参与者的反馈。他在补丁 v5 中添加了一个超调用，用于检索目标实现的版本和支持的 CPU 数量，确保虚拟机能够在迁移过程中正确处理错误。此外，补丁还报告了所有 KVM/arm64 特定的超调用，并根据实现的 CPU 启用相关的错误处理。整体来看，本周的进展主要集中在补丁的细节修改和功能增强上，期待进一步的反馈和测试结果。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下对 CNTHCTL_EL2.EL1NV{P,V}CT 位的传播的补丁（PATCH v2 09/12）。该补丁旨在解决 KVM ARM 中与虚拟化相关的约束问题，确保虚拟机对非易失性（NV）状态的正确处理。

在历史讨论中，Wei-Lin Chang 提出了对 NV 和 E2H 约束的疑问，Marc Zyngier 解释了这些约束在 kvm-arm64/nv-e2h-select 分支中得到了执行，并指出相关代码的复杂性需要进一步研究。此讨论为补丁的背景提供了重要信息。

在本周的新讨论中，Wei-Lin Chang 表达了对 Marc Zyngier 解释的感谢，并表示将深入研究相关代码。此外，Volodymyr Babchuk 提出了在使用该补丁在 Amazon Graviton 4 平台上启动 Xen 时遇到的问题，指出补丁在处理 EL2 定时器状态时存在缺陷，导致 Xen 对定时器的写入被覆盖。Babchuk 询问如何正确修复此问题，并提到在 Dom0 中也观察到了与此相关的定时器问题，但尚未确定具体原因。

总体而言，本周讨论集中在补丁的实际应用及其在特定环境下的潜在问题上，显示出对 KVM ARM 虚拟化支持的复杂性和挑战。

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

本邮件线程讨论了一个针对 KVM（内核虚拟机）在 arm64 架构下的补丁，主题为“将 SVE（可扩展向量扩展）客户机退出处理分解为一个函数”。该补丁旨在改善 SVE 状态的保存和恢复机制。

在历史讨论中，Mark Rutland 提出了一个潜在的隐患，指出在处理 SVE 时可能存在的一个潜在错误，这个错误可能与之前的提交（8c8010d69c132273）有关，该提交涉及 SVE 状态的保存和恢复。Rutland 对于 IRQ（中断请求）在某些情况下的处理表示怀疑，认为需要进一步审查。

在本周的新讨论中，Marc Zyngier 提出是否应提前保存/恢复 ZCR_ELx（SVE 的控制寄存器），并表示如果这是必要的，可以立即进行修改。Rutland 对此表示赞同，并表示会进一步确认并进行相应的调整。

总体来看，本周的讨论集中在如何优化 SVE 状态的处理上，参与者们达成了一致，准备对补丁进行必要的修改以解决潜在问题。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及在初始化 BSS（未初始化数据段）变量后刷新 hypervisor 的 BSS 区域。

**原始补丁内容**：
补丁旨在解决在初始化过程中，hypervisor 无法正确读取 CPU 特性寄存器的值的问题。由于这些值在 BSS 区域中，补丁提议在初始化完成后刷新整个 BSS 区域，以确保 EL2 能够正确访问这些数据。

**之前讨论要点**：
在补丁的背景讨论中，提到由于未能刷新 BSS，导致 EL2 看到的值为 0，从而在后续的上下文切换中引发内核崩溃。补丁的提出是为了避免这种情况。

**本周的新讨论与进展**：
本周的讨论中，参与者对补丁进行了反馈。Marc Zyngier 对补丁的有效性表示怀疑，认为在 hypervisor 初始化后再进行刷新可能并不能解决问题，并指出可能会导致访问违规。Lokesh Vutla 则承认在测试过程中发现了问题，并计划在下一个版本中将刷新操作移至 `kvm_hyp_init_symbols()` 函数中，以确保在 EL2 初始化之前完成刷新。Lokesh 还表示将删除一些冗余的讨论内容，以简化补丁说明。

总的来说，本周的讨论集中在对补丁的有效性和实现细节的审查上，参与者之间的互动推动了补丁的进一步优化。

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

本邮件讨论的主题是关于 kvmtool 的错误处理修复，包含两个补丁。第一个补丁旨在修复 VCPU 线程返回码的传播问题，以便在测试失败时能够正确检测错误。当前实现中，VCPU 0 的返回码未被捕获，导致即使 VCPU 0 出现错误，kvmtool 也可能返回成功状态。修复后，kvmtool 将在 KVM_RUN 中遇到未处理错误时返回非零退出码。

第二个补丁则是针对地址转换失败时的警告信息处理。原本在地址转换失败时会打印警告信息，这在某些情况下可能会造成冗余或误导。补丁将这些警告信息改为调试信息，以减少不必要的输出，并避免混淆。

本周的讨论集中在这两个补丁的具体实现和必要性上，参与者 Alexandru Elisei 提出了补丁的详细背景和预期效果，强调了在集成 kvmtool 与 kvm-unit-tests 自动测试运行器时发现的问题。整体来看，这些修复旨在提升 kvmtool 的错误处理能力和调试信息的清晰度。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及在初始化 BSS（未初始化数据段）变量后刷新 hyp BSS 区域。

**原始 patch/问题的内容**：
补丁的目的是在 hypervisor 初始化变量后，刷新整个 BSS 区域，以确保在 MMU 关闭时，EL2 能够正确访问这些变量。补丁中提到，单独刷新每个变量效率低下，因此选择在初始化完成后一次性刷新整个 BSS 区域。

**之前的讨论要点**：
在历史讨论中，补丁的 v1 版本已被提出，并在此基础上进行了修改，主要更新了提交信息和函数调用。补丁是基于 Linux 6.13 版本的。

**本周的新讨论、进展或结论**：
在本周的讨论中，Lokesh Vutla 提交了补丁的 v2 版本，并得到了参与者 Marc Zyngier 的认可，Marc 表示已将该补丁应用于修复集，并感谢 Lokesh 的贡献。补丁的最终提交 ID 为 9bcbb6104a344d3526e185ee1e7b985509914e90。

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

本邮件线程讨论了针对 KVM 的 Arm SMMUv3 驱动的 RFC PATCH v2，主要关注于 pKVM 的实现和设计。

1. **原始 patch/问题的内容**：该补丁系列旨在为 KVM 提供 Arm SMMUv3 驱动，支持在虚拟化环境中进行设备的地址转换和隔离。讨论中提到，驱动主要针对主机，如何处理来宾的地址映射和隔离是关键问题。

2. **之前的讨论要点**：历史讨论中，参与者探讨了嵌套翻译和半虚拟化的必要性，强调了在不同硬件场景下的性能需求和复杂性。Jason Gunthorpe 提出，pKVM 应该负责 SMMU 硬件的管理，以便为后续功能扩展打下基础。Kevin Tian 关注于如何减少代码重复和维护负担，建议采用分阶段的方法逐步实现。

3. **本周的新讨论、进展或结论**：本周的讨论中，Mostafa Saleh 表示将减少补丁系列的复杂性，专注于 DMA 隔离的实现，并计划在 v3 版本中去除半虚拟化部分。参与者还讨论了 DMA API 的使用场景及其对内存连续性的要求，强调了在移动设备上实现这些功能的挑战。此外，Tian Kevin 提到，pKVM 驱动的复杂性需要在未来的版本中重新评估，以确保其可维护性和适应性。

总的来说，讨论围绕如何在 pKVM 中有效实现 SMMUv3 驱动展开，强调了性能、隔离和代码可维护性的重要性。

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

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 SMMU-v3（系统内存管理单元版本3）命令队列设置的 RFC（请求反馈）补丁。该补丁旨在改进命令队列的管理，以提升虚拟化性能。

在历史讨论中，尚未提供具体的补丁内容或详细的背景信息，因此我们无法得知之前的讨论要点。

在本周的新讨论中，参与者 Robin Murphy 对 Mostafa Saleh 提出的补丁进行了回应，提醒他在实现过程中需要注意重新实现错误修正（errata）工作，以避免生成某些有问题的命令序列。他指出，这些问题在当前的内核驱动中大多是隐含的，暗示着实现过程中可能会遇到的复杂性。

总结来看，本周的讨论主要集中在补丁实施的潜在挑战上，特别是与错误处理相关的细节，强调了在开发过程中需要谨慎对待的技术问题。

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

本邮件线程讨论了 KVM/arm64 在 6.14 版本的更新内容。历史邮件中，Marc Zyngier 提出了针对 6.14 的初步补丁集，主要集中在调试和保护模式的清理工作上。此外，新特性包括对受保护模式下非受保护客户机的支持、EL2 定时器支持以及改进的 CoreSight 支持。补丁还涉及了一些常规的代码清理和错误修复，并提到需要合并两个其他分支以解决一些复杂的冲突。

在本周的新讨论中，Paolo Bonzini 对 Marc 的邮件进行了回复，确认已将这些更新合并，表示感谢。这表明补丁已成功被采纳，进一步推动了 KVM/arm64 的发展。整体来看，本周的讨论主要是对历史讨论的确认和进展更新。

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

本邮件线程讨论了针对 KVM 单元测试的补丁系列，主要是将 kvmtool 添加到测试运行脚本中，以支持 ARM 和 ARM64 架构的测试。

1. **原始补丁/问题内容**：
   该补丁系列（PATCH v2 00/18）旨在将 kvmtool 支持集成到 `run_tests.sh` 脚本中，使得用户可以通过简单的命令运行所有测试。kvmtool 相较于 QEMU 更小且运行速度更快，适合开发者进行原型设计和测试。

2. **之前讨论要点**：
   在历史讨论中，参与者提到 kvmtool 的不同之处，如内存布局和 UART 的不同，并指出某些测试在 kvmtool 上可能无法运行。补丁系列经过重写，分为多个小补丁以便于审查，并添加了新的测试参数和环境变量。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在补丁的具体实现上，包括文档更新、参数重命名、错误处理和对 kvmtool 的支持。参与者对补丁进行了审查，并提出了改进建议，如使用通用的参数名称以减少重复。最终，补丁被确认可以启用 kvmtool 支持，并移除了与 ERRATA_FORCE 相关的配置，以确保测试环境的正确性。整体上，讨论推动了 kvmtool 的集成进程，并为未来的测试提供了灵活性。

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

